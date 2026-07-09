#!/usr/bin/env python3
"""
搜狗微信文章搜索 - 公开公众号文章免登录抓取
用法: python3 sogou_search.py --query "招商银行 招聘" --pages 3
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote, unquote

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("缺少依赖: pip3 install --user --break-system-packages requests beautifulsoup4 lxml")
    sys.exit(1)


UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
URL = "https://weixin.sogou.com/weixin"


def fetch_page(query: str, page: int, session: requests.Session) -> str:
    """抓单页 HTML。"""
    params = {
        "type": 2,            # 2=文章
        "query": query,
        "page": page,
        "ie": "utf8",
    }
    headers = {
        "User-Agent": UA,
        "Referer": "https://weixin.sogou.com/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    r = session.get(URL, params=params, headers=headers, timeout=15)
    r.raise_for_status()
    r.encoding = "utf-8"
    return r.text


def parse_articles(html: str, source_keyword: str) -> list[dict]:
    """从 HTML 解析文章列表。"""
    soup = BeautifulSoup(html, "lxml")
    items = []
    # 搜狗微信文章 li 包含: 标题 / 公众号 / 时间 / 摘要 / 临时链接
    for li in soup.select("li[data-docid], .news-list li, .weui_news_card"):
        # 标题
        title_tag = li.select_one("h3 a, .tit a")
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        # sogou 把真链接放在跳转页, 需要 _decode
        href = title_tag.get("href", "")
        # 公众号
        mp_tag = li.select_one(".all-time-y, .account, .wx-color-default")
        mp = mp_tag.get_text(strip=True) if mp_tag else ""
        # 摘要
        desc_tag = li.select_one("p.txt-info, .txt, .desc")
        desc = desc_tag.get_text(strip=True) if desc_tag else ""
        # 时间戳
        ts_tag = li.select_one(".s-p, .time, .news-date")
        ts = ts_tag.get_text(strip=True) if ts_tag else ""
        # 链接
        link = href if href.startswith("http") else f"https://weixin.sogou.com{href}"

        items.append({
            "title": title,
            "wechat_id": mp,
            "desc": desc[:200],
            "time": ts,
            "url": link,
            "source_keyword": source_keyword,
        })
    return items


def main():
    parser = argparse.ArgumentParser(description="搜狗微信文章搜索")
    parser.add_argument("--query", required=True, help="搜索关键词 (空格分隔)")
    parser.add_argument("--pages", type=int, default=1, help="抓取页数 (每页 10 条)")
    parser.add_argument("--delay", type=float, default=2.5, help="请求间隔秒 (防封)")
    parser.add_argument("--out", help="输出 JSON 文件路径")
    args = parser.parse_args()

    sess = requests.Session()
    all_items = []
    for p in range(1, args.pages + 1):
        try:
            print(f"抓第 {p}/{args.pages} 页: {args.query}", file=sys.stderr)
            html = fetch_page(args.query, p, sess)
            items = parse_articles(html, args.query)
            print(f"  拿到 {len(items)} 条", file=sys.stderr)
            all_items.extend(items)
            time.sleep(args.delay)
        except requests.exceptions.HTTPError as e:
            print(f"  HTTP 错误: {e}", file=sys.stderr)
            # 429/302 都跳过
            break
        except Exception as e:
            print(f"  出错: {e}", file=sys.stderr)
            break

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(all_items, ensure_ascii=False, indent=2))
        print(f"\n保存 {len(all_items)} 条到 {args.out}", file=sys.stderr)
    else:
        print(json.dumps(all_items, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()