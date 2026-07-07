#!/usr/bin/env python3
"""
批量将 data/*.md 中所有"招聘主页链接"替换为"带方向关键词的搜索 URL"。

策略：
- 对每张表格，每行的链接上下文包含"具体方向"（中文）
- 提取该行的"方向"列 → 作为搜索关键词
- 把链接换成 "?keywords={方向}" 这种带搜索词的列表页
"""
import re
import sys
import urllib.parse
from pathlib import Path

DATA_DIR = Path("/home/lizhihao/code/job-pulse/data")

# 不同公司的 URL 模板
URL_TEMPLATES = {
    "字节跳动": "https://jobs.bytedance.com/campus/position?keywords={kw}",
    "阿里巴巴": "https://talent-holding.alibaba.com/campus/position-list?campusType=freshman&keywords={kw}",
    "腾讯": "https://join.qq.com/post.html?query=p_1&keyword={kw}",
    "百度": "https://talent.baidu.com/jobs?keyword={kw}",
    "美团": "https://zhaopin.meituan.com/web/position?keywords={kw}",
    "京东": "https://campus.jd.com/jobs?keyword={kw}",
    "华为": "https://career.huawei.com/reccampportal/portal5/index.html?keyword={kw}",
    "小米": "https://hr.xiaomi.com/campus/list?keyword={kw}",
    "B站": "https://jobs.bilibili.com/positions?keywords={kw}",
    "小红书": "https://campus.xiaohongshu.com/positions?keywords={kw}",
    "知乎": "https://app.mokahr.com/apply/zhihu?keyword={kw}",
    "得物": "https://app.mokahr.com/apply/dewu?keyword={kw}",
    "理想": "https://www.lixiang.com/recruit/position?keyword={kw}",
    # 下列公司未支持 URL 搜索参数，仅保留主页
    # "快手": "https://campus.kuaishou.cn/"  # 进首页再用站内搜索
    # "OPPO": "https://careers.oppo.com/"
    # "vivo": "https://hr.vivo.com/"
    # "大疆": "https://we.dji.com/zh-CN/campus/"
    # "蔚来": "https://campus.nio.com/"
    # "小鹏": "https://www.xiaopeng.com/recruit.html"
    # "拼多多": "https://careers.pinduoduo.com/campus/grad"
    # "携程": "https://careers.trip.com/"
    # "猿辅导": "https://hr.yuanfudao.com/"
    # "喜马拉雅": "https://job.ximalaya.com/"
    # "阅文": "https://recruit.yuewen.com/"
}

# 公司识别：链接 → 公司名
def detect_company(url: str) -> str:
    if "bytedance.com" in url: return "字节跳动"
    if "alibaba.com" in url: return "阿里巴巴"
    if "tencent.com" in url or "qq.com" in url: return "腾讯"
    if "baidu.com" in url: return "百度"
    if "meituan.com" in url: return "美团"
    if "jd.com" in url: return "京东"
    if "huawei.com" in url: return "华为"
    if "kuaishou.cn" in url or "kuaishou.com" in url: return "快手"
    if "pinduoduo.com" in url or "pdd" in url: return "拼多多"
    if "xiaomi.com" in url: return "小米"
    if "oppo.com" in url: return "OPPO"
    if "vivo.com" in url: return "vivo"
    if "dji.com" in url: return "大疆"
    if "nio.com" in url: return "蔚来"
    if "xiaopeng.com" in url: return "小鹏"
    if "lixiang.com" in url: return "理想"
    if "xiaohongshu.com" in url: return "小红书"
    if "bilibili.com" in url: return "B站"
    if "zhihu" in url: return "知乎"
    if "dewu" in url or "poizon" in url: return "得物"
    if "trip.com" in url or "ctrip" in url: return "携程"
    if "yuanfudao" in url: return "猿辅导"
    if "ximalaya" in url: return "喜马拉雅"
    if "yuewen" in url: return "阅文"
    return None

# 提取方向关键词：优先用方向列；否则用当前行的第二个非空 cell
def extract_direction(line: str) -> str:
    # 匹配 markdown 表格行 | a | b | c |
    cells = [c.strip() for c in line.strip().split('|')]
    # cells[0] = '' (开头), cells[-1] = '' (结尾)
    cells = [c for c in cells if c]
    if len(cells) >= 2:
        return cells[0]  # 第一个 cell 是"具体方向"
    return None

def is_job_link(url: str) -> bool:
    """判断是否是"招聘主页/列表页"链接（没有 ID 也没带关键词）"""
    # 排除带 ?keywords= 的（已经是搜索 URL）
    if "?keywords=" in url or "?keyword=" in url or "?" in url and "kw=" in url:
        return False
    # 排除详情页 (含 /position/{ID}/ 或 /position_detail/)
    if re.search(r'/position/\d{16,}/', url):
        return False
    # 排除第三方平台具体岗位 (zhipin job_detail/xx.html)
    if "job_detail/" in url:
        return False
    # 排除 mokahr 的 ?position=xxx
    if re.search(r'position=\d+', url):
        return False
    # 排除 nowcoder 的 ?jobIds=
    if "jobIds=" in url:
        return False
    return True

def rewrite_file(filepath: Path) -> tuple:
    """重写单个 md 文件，返回 (替换数, 总行数)"""
    content = filepath.read_text()
    lines = content.split('\n')
    replaced = 0
    
    for i, line in enumerate(lines):
        # 只处理表格行（以 | 开头）
        if not line.strip().startswith('|'):
            continue
        
        # 提取方向关键词
        direction = extract_direction(line)
        if not direction:
            continue
        # 过滤分隔行 (| --- | --- |)
        if set(direction.replace(' ', '')) <= {'-', '|', ' ', '|'}:
            continue
        # 标题里的"具体方向"可能会被误认；要求长度 2-30
        if not (2 <= len(direction) <= 30):
            continue
        
        # 找出所有 <https://xxx> 形式链接
        def replace_link(m):
            nonlocal replaced
            url = m.group(1)
            if not is_job_link(url):
                return m.group(0)
            
            company = detect_company(url)
            if not company:
                return m.group(0)
            
            template = URL_TEMPLATES.get(company)
            if not template:
                return m.group(0)
            
            kw_encoded = urllib.parse.quote(direction)
            new_url = template.format(kw=kw_encoded)
            replaced += 1
            return f'<{new_url}>'
        
        new_line = re.sub(r'<(https?://[^>]+)>', replace_link, line)
        lines[i] = new_line
    
    new_content = '\n'.join(lines)
    if replaced > 0:
        filepath.write_text(new_content)
    return replaced, len(lines)

def main():
    print(f"{'文件':<40} {'替换数':>8}")
    print("-" * 50)
    total = 0
    for md_file in sorted(DATA_DIR.glob("*.md")):
        count, lines = rewrite_file(md_file)
        if count > 0:
            print(f"{md_file.name:<40} {count:>8}")
            total += count
    print("-" * 50)
    print(f"{'TOTAL':<40} {total:>8}")

if __name__ == "__main__":
    main()