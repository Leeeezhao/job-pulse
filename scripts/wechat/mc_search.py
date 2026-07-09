#!/usr/bin/env python3
"""
JobPulse × MediaCrawler 集成 - 用 MediaCrawler 抓指定平台的校招相关内容
支持平台: xhs / dy / ks / bili / wb / tieba / zhihu
不依赖 CDP, 默认 headless=False (用户首次扫码)

用法:
    # 默认配置: xhs + 校招关键词
    python3 mc_search.py --platform xhs --keywords "算法岗 校招,算法实习 字节"
    
    # 走抖音
    python3 mc_search.py --platform dy --keywords "AI算法 招聘"
"""

import argparse
import subprocess
import sys
from pathlib import Path

# MediaCrawler 安装路径
MC_DIR = Path.home() / "code" / "MediaCrawler"
MC_PY = MC_DIR / ".venv" / "bin" / "python"
MC_MAIN = MC_DIR / "main.py"

# JobPulse 默认校招关键词
DEFAULT_KEYWORDS = [
    "算法岗 校招",
    "AI算法 实习",
    "大模型 招聘",
    "字节 算法 校招",
    "腾讯 算法 内推",
    "百度 算法 实习",
    "推荐算法 招聘",
    "搜推算法",
    "NLP算法 实习",
    "LLM 实习",
]


def run(platform: str, keywords: list[str], login_type: str = "qrcode",
        save_dir: Path = None, max_concurrency: int = 1,
        headless: bool = False) -> int:
    """调 MediaCrawler main.py 抓数据。"""
    if not MC_PY.exists():
        print(f"❌ MediaCrawler venv 未找到: {MC_PY}", file=sys.stderr)
        return 1
    if not MC_MAIN.exists():
        print(f"❌ MediaCrawler main.py 未找到: {MC_MAIN}", file=sys.stderr)
        return 1

    save_data_path = save_dir or Path.home() / "reports" / "mediacrawler" / platform
    save_data_path.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(MC_PY), str(MC_MAIN),
        "--platform", platform,
        "--type", "search",
        "--lt", login_type,
        "--keywords", ",".join(keywords),
        "--save_data_option", "jsonl",
        "--save_data_path", str(save_data_path),
        "--max_concurrency_num", str(max_concurrency),
        "--headless", "false" if not headless else "true",
    ]

    print(">>> " + " ".join(cmd), file=sys.stderr)
    print(f"数据存到: {save_data_path}", file=sys.stderr)
    print(f"提示: 第一次跑会弹出二维码, 请用对应 APP 扫码", file=sys.stderr)
    return subprocess.call(cmd, cwd=str(MC_DIR))


def main():
    parser = argparse.ArgumentParser(description="JobPulse × MediaCrawler")
    parser.add_argument("--platform", default="xhs",
                        choices=["xhs", "dy", "ks", "bili", "wb", "tieba", "zhihu"],
                        help="目标平台 (默认 xhs=小红书)")
    parser.add_argument("--keywords", help="自定义关键词, 英文逗号分隔")
    parser.add_argument("--lt", default="qrcode", choices=["qrcode", "phone", "cookie"])
    parser.add_argument("--headless", action="store_true", help="无头模式")
    parser.add_argument("--save-dir", help="数据保存目录")
    parser.add_argument("--max-concurrency", type=int, default=1)
    args = parser.parse_args()

    if args.keywords:
        kws = [k.strip() for k in args.keywords.split(",") if k.strip()]
    else:
        kws = DEFAULT_KEYWORDS

    rc = run(
        platform=args.platform,
        keywords=kws,
        login_type=args.lt,
        save_dir=Path(args.save_dir) if args.save_dir else None,
        max_concurrency=args.max_concurrency,
        headless=args.headless,
    )
    sys.exit(rc)


if __name__ == "__main__":
    main()