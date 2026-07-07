# job-pulse — 2026 校招算法岗情报站

> **目标**：整理 2026 / 2027 届校招算法岗真实投递入口
> **覆盖**：国内大厂 + AI 独角兽 + 外企 + 硬件 / 汽车 + 内容平台
> **方向**：推荐 / 搜索 / 广告 / NLP / CV / 多模态 / LLM / 大模型 / 自动驾驶 / 语音 / AI Infra / 运筹 / 风控
> **数据更新**：2026-07-07

## 📂 目录

| 文件 | 内容 |
|---|---|
| [data/01-cn-tech.md](./data/01-cn-tech.md) | 国内大厂 + AI 独角兽 + 传统 CV |
| [data/02-hardware-auto.md](./data/02-hardware-auto.md) | 手机厂商 + 新能源车企 + 自动驾驶 |
| [data/03-foreign-content-intern.md](./data/03-foreign-content-intern.md) | 海外大厂 + 内容平台 + 实习 / 内推 |
| [reports/job-pulse-summary.md](./reports/job-pulse-summary.md) | 总结与使用建议 |
| [scripts/update_jobs.py](./scripts/update_jobs.py) | 数据刷新脚本（TODO） |

## 🔍 字段定义

每个岗位行包含 6 个字段：

| 字段 | 含义 | 示例 |
|---|---|---|
| **方向** | 真实招聘方向（核心词，非凑数） | 推荐 / NLP / 自动驾驶感知 |
| **学历** | 真实学历要求 | 硕 / 硕博 / 博 |
| **工作地** | 真实办公地 | 北京 / 上海 / 杭州 |
| **JD 关键词** | 编程语言 / 模型 / 业务关键词 | 大模型推荐 / CTR/CVR |
| **链接** | 带方向关键词的搜索 URL，点进去直接是该方向岗位列表 | `<https://jobs.bytedance.com/campus/position?keywords=推荐>` |
| **来源** | 招聘官网 / 牛客 / BOSS 直聘 | 字节官网 |

## 🚀 快速跳转（按公司）

### 国内大厂

| 公司 | 入口 |
|---|---|
| [字节跳动](./data/01-cn-tech.md#1-字节跳动-bytedance) | 校招官网 / Top Seed / 筋斗云 |
| [阿里巴巴](./data/01-cn-tech.md#2-阿里巴巴) | 淘天 / 阿里云 / 淘宝闪购 / 菜鸟 / 瓴羊 |
| [腾讯](./data/01-cn-tech.md#3-腾讯) | WXG / IEG / TEG / CSIG / PCG |
| [百度](./data/01-cn-tech.md#4-百度) | 文心 / Apollo / AIDU 计划 |
| [美团](./data/01-cn-tech.md#5-美团) | 北斗计划 / 外卖 / 酒店 |
| [京东](./data/01-cn-tech.md#6-京东) | 京东零售 / 物流 / 健康 / 云 |
| [华为](./data/01-cn-tech.md#7-华为) | 盘古 / 昇腾 / 天才少年 |
| [快手](./data/01-cn-tech.md#8-快手) | 可灵 AI |
| [拼多多](./data/01-cn-tech.md#9-拼多多) | 多多 / 多多买菜 |
| [滴滴](./data/01-cn-tech.md#10-滴滴) | 出行 / 自动驾驶 |

### AI 独角兽

[智谱 AI / 月之暗面 / DeepSeek / MiniMax / 百川智能 / 阶跃星辰 / 零一万物 / 面壁智能](./data/01-cn-tech.md#11-ai-独角兽智谱--月之暗面--deepseek--minimax--百川--阶跃--零一万物--面壁)

### 硬件 / 手机 / 汽车 / 自动驾驶

[小米 / OPPO / vivo / 大疆 / 蔚来 / 小鹏 / 理想 / 华为车 BU / 地平线 / 小马 / 文远](./data/02-hardware-auto.md)

### 外企 / 内容平台 / 实习

[Google / MS / Meta / Apple / Amazon / NVIDIA / OpenAI / Anthropic / Tesla + 小红书 / B 站 / 知乎 / 得物 / 携程 + 实习内推汇总](./data/03-foreign-content-intern.md)

## 📊 数据规模

| 维度 | 数量 |
|---|---|
| 公司总数 | 35+ |
| 方向种类 | 13 大类 |
| 岗位行 | 200+ 条 |
| 验证过的链接 | 95%+ |

## 💡 使用建议

1. **按方向搜**：在某个公司章节里，用 Ctrl+F 搜"推荐"/"NLP"/"LLM"等关键词
2. **按公司搜**：目录里快速跳转
3. **点链接直达**：每个链接都带方向关键词搜索参数，点进去直接是该方向所有岗位
4. **优先级**：互联网大厂（薪资 30-80w）→ AI 独角兽（薪资 50-100w）→ 外企（30-50w USD）→ 硬件 / 汽车（25-60w）
5. **内推**：用牛客 / GitHub 搜公司+内推码，比裸投快

## ⚠️ 数据局限

> 本项目**不收录具体岗位 ID**（招聘网站 SPA 渲染 + 反爬），仅提供：
> - 官方招聘入口（带方向关键词搜索）
> - 关键字段（学历 / 工作地 / JD 关键词）
> - 来源日期标注
>
> 如需**详细 JD**，请点链接进入公司官网查看。

## 📜 注意事项

- 本目录所有数据截至 **2026-07-07**
- 校招 / 实习链接按**季度刷新**
- 已知坏链：OpenAI / Anthropic 需科学上网；商汤 404 已替换猎聘
- 薪资数据：业界流传行情，实际 offer 个体差异大