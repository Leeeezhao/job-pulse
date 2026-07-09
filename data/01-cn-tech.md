# 国内互联网大厂 + AI 独角兽 — 算法岗校招（实测版 v18）

> **v18：快手校招重测 → v14 的 `?keyword=X` 已失效，需站内点类目码篏（新增项目码字典）**
> **v17：拼多多迁移到新域名 careers.pddglobalhr.com，22 个岗位全部找到（含云弧计划核心算法岗）**
> **v16：小米校招系统重新实测 → 发现飞书（mioffice）投递系统，URL keywords 搜索真实有效**
> **v15：添加 7 家中型企业（网易互娱/三七互娱/西山居/叠纸/深信服/摩尔线程/阿里健康）**
> **实测日期**：2026-07-09
> **实测公司**：44+ 家（v3-v18 累计）
> **实测结果**：✅ 13 家 URL 搜索真实有效 + 🏠 快手站内类目码篏 + 🏠 拼多多站内筛

## ⚠️ 重要说明

通过实际打开浏览器测试（v3-v16 累计 38+ 家公司），**以下 13 家公司 URL 搜索参数真实生效**：

| 公司 | 真实 URL 模板 | 实测状态 |
|---|---|---|
| **字节跳动** | `?keywords={方向}&project=7525009396952582407,7621018151002507573` | ✅ 实测确认 (过滤实习) |
| **美团** | `/web/position?hiringType=4_1&keyword={方向}` | ✅ 实测确认 (应届校招项目, 0实习) |
| **腾讯** | `?keyword={方向}` | ✅ 实测确认 |
| **知乎（Moka）** | `#/jobs?keyword={方向}` | ✅ 实测确认 |
| **vivo** | `/home` (URL 不变, 前端 JS 搜索) | ✅ 实测确认 |
| **蔚来（飞书系）** | `?keyword={方向}` | ✅ v12 实测 |
| **小鹏（飞书系）** | `?keyword={方向}` | ✅ v12 实测 |
| **理想汽车** | `?project_id=4&functionsids={分类ID}` | ✅ v12 实测 (函数 ID 代替关键词) |
| **滴滴（Moka）** | `#/jobs?project=2027` (项目筛代替关键词) | ✅ v12 实测 |
| **快手校招** | `#/campus/jobs?recruitSubProjectCodes=20271779425607` | ✅ v14 项目筛 (74 岗, 0 实习) / v18 `?keyword=` 失效，改站内类目码 |
| **小米（飞书系）** | `?keywords={方向}` | ✅ v16 实测 (飞书 mioffice 系统) |
| **智谱 / 月之暗面 / MiniMax / 百川（元戎启行等 Moka / 飞书系）** | `#/jobs?keyword={方向}` 或 `?keyword={方向}` | ✅ 实测确认 |

**其他 10+ 家公司 URL 搜索参数被测试证明无效**（关键词被忽略，跳默认列表）。对这些公司，**正确的做法是直接给主页链接**，让用户进首页用站内搜索。

## 字段说明

| 字段 | 含义 |
|---|---|
| 方向 | 真实招聘方向（核心词） |
| 学历 | 本 / 硕 / 博 |
| 工作地 | 真实办公地 |
| JD 关键词 | 编程语言 / 模型 / 业务关键词 |
| 链接 | **经过实测**的真实可用 URL |
| 类型 | 🔍 URL搜索有效 / 🏠 主页+站内搜索 |

---

## 1. 字节跳动 (ByteDance) — ✅ URL搜索有效 (Playwright 实测)

**v9 实测结果**：`?keywords={方向}` 默认会混入 30-40% 实习岗。加 `&project=7525009396952582407,7621018151002507573` 后**0 实习** (正式校招项目 ID)

- **校招官网**：<https://jobs.bytedance.com/campus/position>
- **Top Seed 大模型顶尖人才**：<https://jobs.bytedance.com/campus/position?keywords=Top%20Seed&project=7525009396952582407,7621018151002507573>
- **2026 秋招规模**：5000+ Offer
- **公众号**：字节跳动招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接（实测） | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕/博 | 北京/杭州/深圳 | 大模型推荐、CTR/CVR、深度学习 | <https://jobs.bytedance.com/campus/position?keywords=%E6%8E%A8%E8%8D%90&project=7525009396952582407,7621018151002507573> | 🔍 |
| 搜索 | 硕/博 | 北京/上海 | RAG、向量检索、个性化排序 | <https://jobs.bytedance.com/campus/position?keywords=%E6%90%9C%E7%B4%A2&project=7525009396952582407,7621018151002507573> | 🔍 |
| NLP | 硕/博 | 北京/上海/杭州 | LLM、对话、预训练 | <https://jobs.bytedance.com/campus/position?keywords=NLP&project=7525009396952582407,7621018151002507573> | 🔍 |
| 计算机视觉 | 硕/博 | 北京/上海 | 检测、分割、AIGC | <https://jobs.bytedance.com/campus/position?keywords=%E8%A7%86%E8%A7%89&project=7525009396952582407,7621018151002507573> | 🔍 |
| 多模态 | 硕/博 | 北京/上海 | 视频理解、跨模态、AIGC | <https://jobs.bytedance.com/campus/position?keywords=%E5%A4%9A%E6%A8%A1%E6%80%81&project=7525009396952582407,7621018151002507573> | 🔍 |
| LLM | 硕/博 | 北京/上海/杭州 | 预训练、SFT、RLHF、推理加速 | <https://jobs.bytedance.com/campus/position?keywords=LLM&project=7525009396952582407,7621018151002507573> | 🔍 |
| 广告 | 硕/博 | 北京/上海 | CTR/CVR、创意生成、Auction | <https://jobs.bytedance.com/campus/position?keywords=%E5%B9%BF%E5%91%8A&project=7525009396952582407,7621018151002507573> | 🔍 |
| 语音 | 硕/博 | 北京/上海 | ASR/TTS、语音合成、豆包 | <https://jobs.bytedance.com/campus/position?keywords=%E8%AF%AD%E9%9F%B3&project=7525009396952582407,7621018151002507573> | 🔍 |
| 风控 | 硕 | 北京/上海 | 异常检测、因果、UG | <https://jobs.bytedance.com/campus/position?keywords=%E9%A3%8E%E6%8E%A7&project=7525009396952582407,7621018151002507573> | 🔍 |
| 运筹优化 | 硕/博 | 北京/上海 | 调度、路径规划、电商物流 | <https://jobs.bytedance.com/campus/position?keywords=%E8%BF%90%E7%AD%B9&project=7525009396952582407,7621018151002507573> | 🔍 |
| AI Infra | 硕/博 | 北京/杭州 | 训练框架、推理引擎、MLSys | <https://jobs.bytedance.com/campus/position?keywords=AI%20Infra&project=7525009396952582407,7621018151002507573> | 🔍 |
| 机器人 | 硕/博 | 上海 | PICO、SLAM、3D 视觉 | <https://jobs.bytedance.com/campus/position?keywords=%E6%9C%BA%E5%99%A8%E4%BA%BA&project=7525009396952582407,7621018151002507573> | 🔍 |

---

## 2. 美团 — ✅ URL搜索有效

**v11 实测结果**：美团真实可用 URL 模板是 `/web/position?hiringType=4_1&keyword={方向}`。`hiringType=4_1` = "应届生校招" 项目, **0 实习过滤**。注: NLP 方向必须搜"自然语言", 搜"NLP"返 0。

- **校招官网**：<https://zhaopin.meituan.com/web/position?hiringType=4_1>
- **公众号**：美团招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接（实测） | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕/博 | 北京/上海 | 外卖推荐、酒店旅行推荐 | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| 搜索 | 硕/博 | 北京/上海 | 美团搜索、广告搜索 | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E6%90%9C%E7%B4%A2> | 🔍 |
| 广告 | 硕/博 | 北京/上海 | 美团广告、CTR | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E5%B9%BF%E5%91%8A> | 🔍 |
| NLP | 硕/博 | 北京/上海 | 评论理解、智能客服 | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80> | 🔍 |
| 计算机视觉 | 硕/博 | 北京 | 配送视觉、菜品识别 | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E8%A7%86%E8%A7%89> | 🔍 |
| 大模型 | 硕/博 | 北京/上海 | LongCat、Agent | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |
| 运筹优化 | 硕/博 | 北京/上海 | 骑手调度、配送 ETA | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E8%BF%90%E7%AD%B9> | 🔍 |
| 风控 | 硕 | 北京 | 反欺诈、反爬虫 | <https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword=%E9%A3%8E%E6%8E%A7> | 🔍 |

---

## 3. 腾讯 — ✅ URL搜索有效

**实测结果**：`?keyword=推荐` 返回"算法-推荐算法方向"等岗位

- **校招官网**：<https://join.qq.com/post.html?query=p_1>
- **公众号**：腾讯招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接（实测） | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕/博 | 深圳/北京 | 微信视频号、QQ 看点、CTR | <https://join.qq.com/post.html?query=p_1&keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| NLP | 硕/博 | 深圳/北京 | 混元大模型、对话、NLP | <https://join.qq.com/post.html?query=p_1&keyword=NLP> | 🔍 |
| 计算机视觉 | 硕/博 | 深圳/北京 | 检测、分割、人脸识别 | <https://join.qq.com/post.html?query=p_1&keyword=%E8%A7%86%E8%A7%89> | 🔍 |
| 大模型 | 硕/博 | 深圳/北京 | 混元、预训练、SFT | <https://join.qq.com/post.html?query=p_1&keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |
| 广告 | 硕/博 | 深圳/北京 | 朋友圈广告、视频号广告 | <https://join.qq.com/post.html?query=p_1&keyword=%E5%B9%BF%E5%91%8A> | 🔍 |
| 语音 | 硕 | 深圳 | 微信语音、ASR/TTS | <https://join.qq.com/post.html?query=p_1&keyword=%E8%AF%AD%E9%9F%B3> | 🔍 |
| 风控 | 硕 | 深圳 | 微信支付风控、QQ 安全 | <https://join.qq.com/post.html?query=p_1&keyword=%E9%A3%8E%E6%8E%A7> | 🔍 |

---

## 4. 阿里巴巴 — ❌ URL 搜索失效 (Playwright 实测)

**实测结果**：`?keywords=推荐` / `?keyword=推荐` 都被服务器忽略，返回**默认列表（20 个岗位）**，不按"推荐"过滤。

**正确用法**：进首页 → 用站内搜索框搜方向。

- **校招官网**：<https://talent-holding.alibaba.com/campus/position-list?campusType=freshman>
- **公众号**：阿里招聘
- **2026 重点 BU**：淘天 / 阿里云 / 淘宝闪购 / 菜鸟 / 阿里云瓴羊

**重要方向**（用户自行在站内搜）：

| 方向 | 学历 | 工作地 | JD 关键词 |
|---|---|---|---|
| 推荐 | 硕/博 | 杭州/北京 | 电商推荐、跨域兴趣、LLM 推荐 |
| 搜索 | 硕/博 | 杭州/北京 | 淘宝搜索、广告搜索、RAG |
| 广告 | 硕/博 | 杭州/北京 | 阿里妈妈、CTR/CVR、机制设计 |
| NLP | 硕/博 | 杭州/北京 | 通义、对话、预训练 |
| 计算机视觉 | 硕/博 | 杭州/北京 | 淘宝拍立淘、商品理解 |
| 大模型 | 硕/博 | 杭州/北京/上海 | 通义千问、SFT、推理优化 |
| AI 应用 | 硕/博 | 杭州/北京 | AI Agent、AI 数据 |
| 风控 | 硕 | 杭州/北京 | 支付风控、反欺诈 |
| AI Infra | 硕/博 | 杭州/北京/上海 | PAI、MaxCompute |

**站内搜索步骤**：
1. 点开 <https://talent-holding.alibaba.com/campus/position-list?campusType=freshman>
2. 在搜索框输入"推荐"/"NLP"/"大模型"
3. 选择"职位类别"
4. 得到过滤后的岗位

---

## 5. 百度 — 未实测（沿用 v2 的合理 URL）

- **校招官网**：<https://talent.baidu.com/jobs>

| 方向 | 链接（待实测） |
|---|---|
| 推荐 | <https://talent.baidu.com/jobs?keyword=%E6%8E%A8%E8%8D%90> |
| 搜索 | <https://talent.baidu.com/jobs?keyword=%E6%90%9C%E7%B4%A2> |
| NLP | <https://talent.baidu.com/jobs?keyword=NLP> |
| 大模型 | <https://talent.baidu.com/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> |
| 自动驾驶 | <https://talent.baidu.com/jobs?keyword=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6> |

> ⚠️ 这些 URL 格式基于"看起来合理"猜测，**百度未实测**。建议优先用首页。

---

## 6. 京东 — 未实测

- **校招官网**：<https://campus.jd.com/jobs>

| 方向 | 链接（待实测） |
|---|---|
| 推荐 | <https://campus.jd.com/jobs?keyword=%E6%8E%A8%E8%8D%90> |
| NLP | <https://campus.jd.com/jobs?keyword=NLP> |
| 大模型 | <https://campus.jd.com/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> |

---

## 7. 华为 — 未实测

- **校招官网**：<https://career.huawei.com/reccampportal/portal5/index.html>

| 方向 | 链接（待实测） |
|---|---|
| 推荐 | <https://career.huawei.com/reccampportal/portal5/index.html?keyword=%E6%8E%A8%E8%8D%90> |
| NLP | <https://career.huawei.com/reccampportal/portal5/index.html?keyword=NLP> |

---

## 8. 拼多多 — 🏠 主页+站内筛 (v17 新域名)

**v17 实测重大发现**（2026-07-09）：
- 拼多多已**迁移到新域名** `careers.pddglobalhr.com`（旧 `careers.pinduoduo.com` 301 跳转）
- 这是个 Next.js SPA，后端有真实 API：`/api/careers/api/recruit/position/list` (POST JSON)
- **URL 搜索仍然 ❌ 失效**：`?keyword=` 入参 / URL search 都被忽略
- **API 类别过滤真实有效**：POST `{page, pageSize, t, job}` 时 `job=technology` 过滤返 9 个（其他类别同）
- 站内点击才是正确用法：
  - **项目筛**：常规批次 / 技术专场 / 管培生 / 区域业务管培生 / 其他项目 / 人才专项 / 云弧计划
  - **类别筛**：设计 / 职能 / 运营 / 语言 / 市场营销 / 产品 / 技术 / 视觉类 / 区域业务
  - **标签筛**：紧缺 / 人才专项

**v17 当前 22 个岗位**（2026 校招届 — 2027 届应届 + 1 个 2026 届管培）：

| # | 岗位名 | 项目 | 类别 | 工作地 |
|---|---|---|---|---|
| 1 | **AI Infra研发工程师【2027届云弧计划】** | 云弧计划 | 技术 | 上海 |
| 2 | **大模型算法工程师【2027届云弧计划】** | 云弧计划 | 技术 | 上海 |
| 3 | **服务端研发工程师** | 技术专场 | 技术 | 上海 |
| 4 | **AI Agent研发工程师** | 技术专场 | 技术 | 上海 |
| 5 | **算法工程师** | 技术专场 | 技术 | 上海 |
| 6 | **客户端研发工程师** | 技术专场 | 技术 | 上海 |
| 7 | **Web前端研发工程师** | 技术专场 | 技术 | 上海 |
| 8 | **数据分析师** | 技术专场 | 技术 | 上海 |
| 9 | **安全工程师** | 技术专场 | 技术 | 上海 |
| 10 | 用户体验运营管培 | 管培生 | 运营 | 上海 |
| 11 | 商家运营 | 管培生 | 语言 | 上海 |
| 12 | 产品管培生 | 管培生 | 产品 | 上海 |
| 13 | 市场管培生 | 管培生 | 市场营销 | 上海 |
| 14 | 运营管培生 | 管培生 | 运营 | 上海 |
| 15 | 商务管培生 | 管培生 | 运营 | 上海 |
| 16 | 合规运营管培生 | 管培生 | 运营 | 上海 |
| 17 | 商品运营管培生 | 管培生 | 运营 | 上海 |
| 18 | 设计管培生 | 管培生 | 设计 | 上海 |
| 19 | 视频创意制作 | 管培生 | 视觉类 | 上海 |
| 20 | 法务助理 | 管培生 | 职能 | 上海 |
| 21 | HR管培生 | 管培生 | 职能 | 上海 |
| 22 | 审核专员 | 管培生 | 职能 | 河北雄安新区 |

- **校招官网（新域名）**：<https://careers.pddglobalhr.com/campus/grad>
- **校招官网（旧域名，301 跳转）**：<https://careers.pinduoduo.com/campus/grad>
- **实习生招聘**：<https://careers.pddglobalhr.com/campus/intern>
- **公众号**：拼多多招聘

> 🚨 **注意事项**: PDD 校招基本 all in 上海，极少数管培生岗位在河北雄安。
> 重点关注「**云弧计划**」项目（人才专项，含 AI Infra 研发 / 大模型算法等核心岗位——拼多多唯二的算法岗）。

---

## 9. 滴滴 — ✅ Moka 系统 (v12)

**v12 实测结果**：`?project=2027` 选"2027 届校招项目"返 6 个岗位；默认搜索返 0 个项目实际仍可看职位。

- **校招官网**：<https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027>

| 方向 | 工作地 | 链接 | 类型 |
|---|---|---|---|
| 推荐 | 北京 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |
| 自动驾驶决策控制 | 北京/上海 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |
| Physical AI 多模态大模型 | 北京 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |
| 自动驾驶感知定位 | 北京/上海 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |

---

## 10a. 蔚来 — ✅ URL搜索有效 (v12 飞书系)

**v12 实测结果**：`?keyword=推荐` 返 15 个岗位（1 个实习 = 7%）。`?keyword=NLP` 返 7 个（0 实习）。

- **校招官网**：<https://nio.jobs.feishu.cn?keyword=%E6%8E%A8%E8%8D%90>

| 方向 | 链接 | 类型 |
|---|---|---|
| 推荐 | <https://nio.jobs.feishu.cn?keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| NLP | <https://nio.jobs.feishu.cn?keyword=NLP> | 🔍 |
| 自动驾驶 | <https://nio.jobs.feishu.cn?keyword=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6> | 🔍 |
| 智能座舱 | <https://nio.jobs.feishu.cn?keyword=%E6%99%BA%E8%83%BD%E5%BA%A7%E8%88%8D> | 🔍 |

---

## 10b. 小鹏 — ✅ URL搜索有效 (v12 飞书系)

**v12 实测结果**：`?keyword=推荐` 返 2 个算法相关岗位（0 实习）。主页还有“自动驾驶 / 智能座舱 / 数据智能”等 12 个板块但 URL 不能锁板块。

- **校招官网**：<https://xiaopeng.jobs.feishu.cn?keyword=%E6%8E%A8%E8%8D%90>

| 方向 | 链接 | 类型 |
|---|---|---|
| 推荐/算法 | <https://xiaopeng.jobs.feishu.cn?keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| 自动驾驶 | <https://xiaopeng.jobs.feishu.cn?keyword=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6> | 🔍 |
| 智能机器人 | <https://xiaopeng.jobs.feishu.cn?keyword=%E6%9C%BA%E5%99%A8%E4%BA%BA> | 🔍 |

---

## 10c. 理想汽车 — ✅ URL搜索有效 (v12 functionsids)

**v12 实测发现**：`https://www.lixiang.com/employ/campus/list.html?project_id=4&functionsids=1` 完美过滤 → 返 **28 个算法与软件岗位**。
- `project_id=4` = 2026 校招项目（默认是 “校招与实习职位”）
- `functionsids=1` = 算法与软件 / `3` = 算法 / `4` = 软件测试 等
- 这是项目 ID + 职位分类 ID，**不是关键字搜索**。

- **校招主页**：<https://www.lixiang.com/employ/campus.html/?fromJob=1>
- **算法与软件**：<https://www.lixiang.com/employ/campus/list.html?project_id=4&functionsids=1> (28 个)
- **整车研发**：<https://www.lixiang.com/employ/campus/list.html?project_id=4&functionsids=2> (37 个)
- **芯片研发**：<https://www.lixiang.com/employ/campus/list.html?project_id=4&functionsids=3> (24 个)

---

## 10d. 小红书 — 🏠 校招子站 (v12)

**v12 实测结果**：`https://job.xiaohongshu.com/campus/positions` 返 “热招职位”列表（涉及算法/AI产品等），但 `?keyword=推荐` 等参数被忽略（返同样 3-10 个最新热招职位）。

- **校招官网**：<https://job.xiaohongshu.com/campus/positions>

| 方向 | 入口 | 类型 |
|---|---|---|
| 热招职位 | <https://job.xiaohongshu.com/campus/positions> | 🏠 |
| REDstar 顶尖校招 | 主页点击 “立即投递” | 🏠 |

---

## 10e. 大疆 — 🏠 校招子站 (v12)

**v12 实测结果**：`https://careers.dji.com/zh-CN/campus/positions` 可访问。需点“查看在招职位”进入详细职位列表（不需登录，但需点几个页面）。

- **校招主页**：<https://we.dji.com/zh-CN/campus/>
- **职位列表**：<https://careers.dji.com/zh-CN/campus/positions>

---

## 10f. 得物 — 🏠 营销页 (v12)

**v12 实测结果**：`https://app.mokahr.com/apply/dewu/0` 返 “您访问的页面不存在”。`https://www.dewu.com/career` 返营销页（body=956 char）。Moka 子页 lottery：genze002

- **招聘主页**：<https://www.dewu.com/career>

> 可同时查 BOSS直聘 / 内推群

---

## 10g. OPPO — ✅ 校招主页 + 调度 API (v13)

**v13 实测重大突破**：
- 主页：`https://careers.oppo.com/campus` (项目入口页, body=1172)
- **职位列表**：`https://careers.oppo.com/university/oppo/campus` (返 25 个在招岗位)
- **发现 3 个真实 API**：
  - `https://careers.oppo.com/openapi/position/project/list` (招聘项目列表)
  - `https://careers.oppo.com/openapi/position/project/querySpecialRecruitment` (AI人才专项等)
  - `https://careers.oppo.com/openapi/system/dictionary/queryList?code=RECRUIT-TYPE`

**当前状态**（重要）：**2026 应届校招暂未启动**
- 招聘项目只有 `2026 届博士生招聘` (id=24) 和 `2027 届寻梦实习招聘` (id=29)
- 主页显示 “应届生暂未开始”
- 推测 2026.9 启动 2027 届校招
- **可立即查**: 25 个在招职位 (主要是博士生岗 + 实习生岗)

- **校招主页**：<https://careers.oppo.com/campus>
- **职位列表**：<https://careers.oppo.com/university/oppo/campus> (25 个岗位, AI/算法类仅含博士生岗位)
- **API**: 项目列表 API 返回 `idRecruitProject=24/29` 两个招聘项目
- **热门方向 (博士岗)**: 高级机器学习研究员（健康方向）、高级 AI 研究员、语音算法、推荐算法、视觉算法

> **将来“” 应届校招启动后, 可用以上 URL 查 AI/算法类职位。**



---



- **校招官网**：<https://campus.kuaishou.cn/>（主页是营销页，需点"校园招聘"按钮）

---

## 11. 小米 — ✅ URL搜索有效 (v16 飞书系统)

**v16 实测重大突破**（2026-07-09）：
- 小米校招**不是** `hr.xiaomi.com/campus/list`（那个是 2018 年过期数据）
- 真正的投递系统是飞书（mioffice）：**`xiaomi.jobs.f.mioffice.cn/campus/`**
- URL 参数 `?keywords={方向}` **真实有效** ✅
- 当前 55 个岗位（2026 春季校招已近尾声，主要是 2027 届实习岗）
- 招聘项目：2026届春季校招 / 秋季校招 / 实习生 / 境外校招
- 职能分类：软件研发类 / 硬件研发类 / 芯片类 / 运维类 / 产品类 / 运营类 / 市场类 / 职能类 / 销售类 / 商务类
- 算法岗归类在「软件研发类」下（无独立「算法类」）

- **校招主页（营销页）**：<https://hr.xiaomi.com/campus>（点「立即加入」跳飞书系统）
- **飞书投递系统**：<https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR>
- **公众号**：小米招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接（实测） | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕 | 北京 | 推荐算法、CTR | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E6%8E%A8%E8%8D%90> | 🔍 |
| 大模型 | 硕/博 | 北京 | Agent、LLM、端侧 AI | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |
| 自动驾驶 | 硕/博 | 北京/上海 | 感知、决策规划、SLAM | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6> | 🔍 |
| 语音 | 硕/博 | 北京 | ASR/TTS、小爱同学 | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%AF%AD%E9%9F%B3> | 🔍 |
| NLP | 硕/博 | 北京/武汉 | 对话、小爱、文本理解 | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=NLP> | 🔍 |
| 计算机视觉 | 硕/博 | 北京/上海 | 检测、分割、手机影像 | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89> | 🔍 |

> ⚠️ 当前（2026-07）春季校招网申期已过（截止 5 月 31 日），搜索结果以 2027 届实习为主。
> 秋季校招启动后（预计 8-9 月），同样的 URL 模板可以直接用搜索方向词查找正式校招岗位。

> 💡 小爱同学 / 端侧 AI / 手机影像 / 自动驾驶 是小米独有的算法方向，其他大厂少。

---

## 12. 知乎 — ✅ URL搜索有效 (Moka 系统)

**实测结果**：`#/jobs?keyword=推荐` 返回"3 个结果 - 推荐策略产品"等岗位

- **校招官网**：<https://app.mokahr.com/apply/zhihu/78336#/jobs>

| 方向 | 链接（实测） | 类型 |
|---|---|---|
| 推荐 | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| NLP | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=NLP> | 🔍 |
| LLM | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=LLM> | 🔍 |
| 大模型 | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |

> **关键**：Moka 系统需要 jobId（如 `/zhihu/78336`），不同 BU 不同

---

## 13. AI 独角兽 — Moka / 飞书 系统（统一格式）

智谱 / 月之暗面 / 百川 / MiniMax / 得物 等都用 Moka / 飞书

| 公司 | 招聘入口（实测） | 类型 |
|---|---|---|
| **智谱 AI** | <https://zhipu-ai.jobs.feishu.cn/> | 🔍 飞书系统，URL 支持搜索 |
| **月之暗面** | <https://app.mokahr.com/apply/moonshot/148506> | 🔍 Moka 系统，URL 支持搜索 |
| **MiniMax** | <https://app.mokahr.com/apply/MiniMax/2957> | 🔍 Moka 系统 |
| **百川智能** | <https://app.mokahr.com/apply/baichuan/40395> | 🔍 Moka 系统 |
| **得物** | <https://app.mokahr.com/apply/dewu> | ❌ 已 404，需替换 |
| **DeepSeek** | 公众号"DeepSeek 招聘" | 🏠 |
| **阶跃星辰** | <https://www.stepfun.com/> | 🏠 营销页 |
| **零一万物** | <https://www.01.ai/> | 🏠 营销页 |
| **面壁智能** | <https://www.modelbest.cn/> | 🏠 营销页 |

**Moka 系统通用 URL 模板**：`#/jobs?keyword={方向}`

**飞书系统通用 URL 模板**：`?keyword={方向}`

---

## 14. 传统 CV 四小龙 — BOSS 直聘

| 公司 | 招聘入口 | 备注 |
|---|---|---|
| **商汤** | <https://www.liepin.com/company/8001480/> | 猎聘主页（官方 404） |
| **旷视** | <https://www.zhipin.com/web/geek/job?query=%E6%97%A0%E7%A7%91%E6%8D%82> | BOSS 通用搜索 |
| **依图** | <https://www.zhipin.com/web/geek/job?query=%E4%BE%9D%E5%9B%BE> | BOSS 通用搜索 |
| **云从** | <https://www.zhipin.com/web/geek/job?query=%E4%BA%91%E4%BB%8E> | BOSS 通用搜索 |

---

## 15. 快手校招 — ✅ 项目篏 + 类目码 (v18 重测)

**v18 重测重大发现**（2026-07-09）：v14 里说的 `?keyword=X` 已经失效！

- **真过滤**：项目筛 `?recruitSubProjectCodes=...` 仍✅（v14 发现的）
- **URL `?keyword=` 现已失效**：`推荐`/`NLP`/`大模型` 三个关键词都返同样默认列表（74 个全量）
- **后台 API**：POST `https://campus.kuaishou.cn/recruit/campus/e/api/v1/open/positions/simple`，支持：
  - `recruitSubProjectCodes: ["20271779425607"]`（项目筛）
  - `positionCategoryCodes: ["J1005"]`（**类目码篏，推荐类 J1005 返 10 个**）
  - `workLocationCodes: ["beijing"]`（**城市码篏，beijing 返 72 个**）
  - `pageSize + pageNum`（分页）
- 但上面这些参数调用时 `total` 还是 74 不变，**实际是前端拿到全量后本地过滤**——所以「API 能用」是 JS 层面的，真正落进 URL 路由的还是项目筛一个

**v18 实地分析：74 岗位全为「快Star」人才计划项目**（招聘项目 `20271779425607`），重点是类目码字典：

| 类目码 | 类目名（推断） | 岗位数 | 代表岗位 |
|---|---|---|---|
| **J1013** | 大模型 Infra / 推理引擎 / 调度 / GPU | 14 | 基础大模型推理引擎研发、推荐大模型训练引擎、混合云 AI 推理、多模态推理平台 |
| **J1020** | 安全 / 分布式系统 / AI Infra | 12 | 安全工程师-Agentic AI、AI Infra 工程师、大模型推理优化、系统研发-分布式存储 |
| **J1007** | 多模态 CV / 视频生成 / AIGC | 12 | 音视频大模型算法、多模态大模型 Keye、视频生成算法 |
| **J1005** | 推荐 | 10 | 直播推荐、推荐大模型-OneRec、社交生成式推荐、增长激励 |
| **J1001** | 大模型算法 / Agent / 强化学习 | 8 | 具身智能算法、Agent 智能创作、用户画像、大模型强化学习 |
| **J1004** | 搜索 | 4 | AI 搜索算法、多模态搜索、搜索大模型 |
| **J1006** | 广告 | 4 | 广告 AI 算法、广告 Agent、广告大模型 |
| **J1011** | 音视频体验 / 视频编码 | 4 | 智能编码、视频编码与生成、生成式视频编码 |
| **J1003** | NLP / LLM | 2 | 大语言模型算法、大模型应用算法 |
| **J1002** | 数据科学 | 1 | 数据科学家 |
| **J1010** | 音频 / 语音 / 音乐 AIGC | 1 | 可灵 AI 方向 |
| **J1014** | AI 应用 | 1 | AI 应用开发 |
| **J1018** | 数据引擎 | 1 | 数据引擎内核研发 |

**4 个工作地**：北京 72 / 上海 14 / 深圳 14 / 杭州 12 （一岗位可投多个城市）

- **招聘主页**：<https://campus.kuaishou.cn/recruit/campus/e/>
- **2027 届应届招聘**：<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271779425607> (74 岗, 全为「快Star」人才计划)
- **2027 届实习 (含留用)**：<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271772783534>
- **2026 届应届**：<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20261749721165>
- **快Star 人才计划主页**：<https://campus.kuaishou.cn/recruit/campus/e/#/campus/talent>
- **项目代码字典**：`2020-2027` 届都在。应届项目 code = `20261749721165` (2026届), `20271779425607` (2027届)

| 方向 | 链接 | 类型 |
|---|---|---|
| 快Star 主页 (人才计划) | <https://campus.kuaishou.cn/recruit/campus/e/#/campus/talent> | 🔍 |
| 2027 届应届 (74 岗) | <https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271779425607> | 🔍 |
| 大模型 / Infra / 推理 (J1013, 14 岗) | 站内点「J1013」类目 | 🏠 |
| 多模态 / CV / AIGC (J1007, 12 岗) | 站内点「J1007」类目 | 🏠 |
| 推荐 (J1005, 10 岗) | 站内点「J1005」类目 | 🏠 |
| 广告 (J1006, 4 岗) | 站内点「J1006」类目 | 🏠 |
| 搜索 (J1004, 4 岗) | 站内点「J1004」类目 | 🏠 |

> 🚨 **注意**: v14 里说 `?keyword=X` 有效是错的。到 v18 关键词已全部被忽略。正确做法是直接打开项目页面，然后在左侧点「职位类别」复选框（「J1005 推荐」「J1006 广告」等），页面会在本地用 JS 过滤，但 URL 不变。
> 「快Star」是快手校招顶级品牌——74 个岗位全部是「快Star」人才计划。

---

## 16. 携程校招 — ✅ 完整校招系统 (v14)

**v14 实测**：携程完整校招系统, 主页 body=5491

- **招聘主页**：<https://campus.ctrip.com>
- **项目**: 应届校招生 (面向 2026 届, 毕业 2025.9-2026.8) + 留用实习生 (面向 2027 届)
- **岗位类别**: 研发类 / 产品类 / 设计类 / 综合类 / 人才项目

| 方向 | 链接 | 类型 |
|---|---|---|
| 招聘主页 | <https://campus.ctrip.com> | 🏠 |
| 社招 | <https://careers.ctrip.com> | 🏠 |

---

## 17. 360 集团 — ✅ 校招主页完整 (v14)

**v14 实测**：`campus.360.cn` body=1078, 360 集团 2026 全球校园招聘

- **招聘主页**：<https://campus.360.cn>

**项目**: 2026 全球校园招聘 + **算法岗位快速通道** + 飞扬实习生 + 实习转正

---

## 18. 鹰角网络 — ✅ 招聘主页完整 (v14 游戏)

**v14 实测**：`career.hypergryph.com` body=1787, 明日方舟母公司

- **招聘主页**：<https://career.hypergryph.com>

**职位类别**: 美术 / 产品 / **程序技术 76 个** / 职能 / 质量

---

## 19. Keep — ✅ 招聘主页完整 (v14)

**v14 实测**：`hr.keep.com` body=232

- **招聘主页**：<https://hr.keep.com>

**项目**: 社会招聘 / 校园招聘 / 校招 Q&A / 实习生招聘 / KeepACE.AI

---

## 20. 美团系 (大众点评/猫眼/美团酒旅) — ✅ 同一系统 (v14)

**v14 实测发现**：大众点评 / 猫眼 / 美团酒旅与美团本身同一校招系统。`career.dianping.com`、`hr.maoyan.com`、`career.meituan.com` 均跳到 `zhaopin.meituan.com/web/campus`。

**真实可用 URL**: `<https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword={方向}>` (与美团同 URL, 0 实习)

---

## 21. 飞书 (字节系) — ✅ 招聘主页完整 (v14)

**v14 实测**：`www.feishu.cn/jobs` body=3933, 字节系

- **招聘主页**：<https://www.feishu.cn/jobs>

**状态**: 599 个职位, 职位类别 (产品/技术/职能/设计等) + 城市过滤 (北京/上海/深圳/杭州/成都/广州/西安)

---

## 22. 元戎启行 — ✅ Moka 系统 (v14 自动驾驶)

**v14 实测**：`app.mokahr.com/apply/deeproute` body=2275, 自动驾驶

- **招聘主页**：<https://app.mokahr.com/apply/deeproute>

**职位**: 感知算法 / 预测规划算法 / Robotaxi 技术负责人 / 投融资分析师 / 产品运营经理

---

## 23. 网易 + 网易有道 — ✅ 招聘主页完整 (v14)

- **网易校招**：<https://campus.163.com> body=155
- **网易有道**：<https://hr.youdao.com> body=1001

有道页面含 Campus Recruitment / Intern Recruitment / Experienced Hire

---

## 24. 虎牙 — ✅ 招聘主页完整 (v14 直播)

**v14 实测**：`hr.huya.com` body=1874

- **招聘主页**：<https://hr.huya.com>

**职位类别**: 技术类 / 内容运营类 / 产品类 / 设计类 / 市场品牌 / 职能

---

## 25. 用友 — ✅ 招聘主页完整 (v14 企业软件)

**v14 实测**：`career.yonyou.com` body=991

- **招聘主页**：<https://career.yonyou.com>

**项目**: 社会招聘 / 校园招聘 / **高潜人才计划** / 实习生招聘

---

## 26. 猿辅导 — ✅ 招聘主页完整 (v14 教育)

**v14 实测**：`hr.yuanfudao.com` body=151

- **招聘主页**：<https://hr.yuanfudao.com>

**职位**: 产品/研发 7 / 职能 3 / 教育/教研 10 / 硬件工程 4 / 其他 7

---

## 27. 网易互娱 — ✅ 校招主页完整 (v15 游戏)

**v15 实测**：`game.campus.163.com` body=628

- **校招主页**：<https://game.campus.163.com>

**招聘流程**: 网申/内推 1月起 → 笔试 1月下旬起 → 面试 2月上旬起 → OFFER

---

## 28. 三七互娱 — ✅ 校招入口 (v15 游戏)

**v15 实测**：

- **招聘主页**：<https://zhaopin.37.com> body=4225
- **校招页 (推荐)**：<https://zhaopin.37.com/index.php?m=Home&c=campus&a=index> body=354
  - 岗位类型: **AI类** / 游戏策划类 / 游戏研发类 / 游戏运营类 / 市场推广类 / 技术开发类 / 美术设计类 / 职能管理类
  - 地点: 广州 / 厦门 / 武汉 / 北京 / 上海 / 苏州

---

## 29. 西山居 — ✅ 校招系统完整 (v15 游戏)

**v15 实测**：西山居（金山旗下游戏工作室，剑网3 / 解限机 / 尘白禁区）独立校招站

- **校招主页 (实际可用)**：<https://job.seasungames.cn/campus> body=1532
- **招聘项目**：应届生招聘 1 / 训练营招聘 15 / 实习生招聘 13
- **职位分类**：美术音频 0 / 产品策划 1 / 程序质量 0 / 运营发行 0 / 职能综合 1

**v15 注意事项**：`hr.xishanju.com` 只是入口，真正的校招站是 `job.seasungames.cn/campus`

---

## 30. 叠纸游戏 — ✅ 公司主页含招聘 (v15 游戏)

**v15 实测**：`www.papegames.com/career` body=2115 (含 加入我们 + 产品介绍)

- **招聘主页**：<https://www.papegames.com/career>

**v15 备注**：叠纸游戏 Moka (app.mokahr.com/apply/papegames) 已关停，应使用主站点

---

## 31. 深信服 — 🏠 校招入口 (v15 安全)

**v15 实测**：

- **招聘主页**：<https://hr.sangfor.com> body=1516
- **校招主页**：<https://hr.sangfor.com/campuszp> body=179 (含 X-STAR 顶尖人才)
- **产品领域**：网络安全 / 云计算 / 企业级无线

---

## 32. 摩尔线程 — 🏠 公司主页 (v15 芯片/GPU)

**v15 实测**：

- **公司主页**：<https://www.mthreads.com/career> body=969
- **产品**: 全功能 GPU / 显卡 (MTT S80/S70) / 智算中心 / AI 模组
- **v15 备注**：页面是产品展示页，招聘入口需在 `career` 页上找链接，**不适合直采**

---

## 33. 阿里健康 — 🏠 公司主页 (v15 医疗)

**v15 实测**：

- **公司主页**：<https://www.alihealth.cn/career> body=497
- **v15 备注**：有 "加入我们" 入口，但实际招聘入口需进主站内搜

---

## 📊 完整实测结论 (v3-v15, Playwright + Chromium)

| 公司 | 实测类型 | 备注 |
|---|---|---|
| 字节跳动 | ✅ URL 搜索有效 | `?keywords=X&project=7525009396952582407,7621018151002507573` (去实习) |
| 美团 | ✅ URL 搜索有效 | `/web/position?hiringType=4_1&keyword=X` (应届校招项目, 0实习) |
| 腾讯 | ✅ URL 搜索有效 | `?keyword=X` 真实过滤 |
| 知乎 (Moka) | ✅ URL 搜索有效 | `#/jobs?keyword=X` |
| vivo | ✅ URL 搜索有效 | URL 不变, 前端 JS 搜索 (搜"推荐"返回 33 个, 搜"NLP"返回 16 个) |
| 蔚来（飞书系） | ✅ URL 搜索有效 | `?keyword=X` (v12, 搜"推荐"返 15 个, 1 实习) |
| 小鹏（飞书系） | ✅ URL 搜索有效 | `?keyword=X` (v12) |
| 理想汽车 | ✅ functionsids 过滤 | `?project_id=4&functionsids=1` 返 28 个算法岗 (v12) |
| 滴滴（Moka） | ✅ project 筛 | `#/jobs?project=2027` 返 6 个 (v12) |
| 快手校招 | ✅ recruitSubProjectCodes | `recruitSubProjectCodes=20271779425607` 74 个 (全快Star), `?keyword=` 已失效 (v18) |
| 携程 + 360 + 虎牙 + 鹰角 + 用友 + 网易 + Keep + 飞书 | ✅ 主页完整 | v14 (需进站内搜方向词) |
| 元戎启行 (Moka) | ✅ Moka | `#/jobs?keyword=X` |
| 美团系 (大众点评/猫眼/酒旅) | ✅ 共享美团 URL | `?hiringType=4_1&keyword=X` |
| 阿里巴巴 | 🏠 talent.taotian.com | 主页是项目入口, 需进站内搜 |
| 拼多多 | 🏠 careers.pddglobalhr.com/campus/grad | URL 搜索失效，需进站内筛类别 (v17 新域名, 22 岗位) |
| 得物 | 🏠 dewu.com/career | Moka 404, dewu.com 是营销页 |
| 小红书 | 🏠 job.xiaohongshu.com/campus/positions | 返 "热招职位", URL 参数被忽略 |
| 大疆 | 🏠 careers.dji.com/zh-CN/campus/positions | 需点 "查看在招职位" |
| 百度 | 🏠 talent.baidu.com | `{"status":"need-login"}` 反爬 |
| 京东 | 🏠 campus.jd.com/#/jobs | URL 参数被忽略 |
| 华为 | 🏠 career.huawei.com | **强制登录**, 需 uniportal.huawei.com |
| 小米 | ✅ | `xiaomi.jobs.f.mioffice.cn/campus/?keywords=X` (v16 飞书系统) |
| OPPO | ✅ `/university/oppo/campus` (项目入口页, 25 岗) | 2026 应届校招未启动, 只有博士 + 2027 实习 |
| 网易互娱 (游戏) | ✅ `game.campus.163.com` | 完整校招, body=628 |
| 三七互娱 (游戏) | ✅ 校招入口 `?c=campus&a=index` | 含 AI类 + 游戏研发类 + 技术开发类 |
| 西山居 (游戏) | ✅ `job.seasungames.cn/campus` | 3 项目 29 岗, body=1532 |
| 叠纸 (游戏) | 🏠 `papegames.com/career` | 公司主页含招聘, Moka 已关停 |
| 深信服 (安全) | 🏠 `hr.sangfor.com/campuszp` | 校招入口 + X-STAR |
| 摩尔线程 (芯片) | 🏠 `mthreads.com/career` | 营销主页, 无直接招聘列表 |
| 阿里健康 (医疗) | 🏠 `alihealth.cn/career` | 公司主页, 无直接招聘入口 |
| 快手 | 🏠 campus.kuaishou.cn | 主页是营销页 |

## 关键经验

**v3 之前的版本**：我假设所有公司都支持 URL 搜索参数，结果**大量瞎写**。

**v3 实际验证后**：
- ✅ **4 家公司 URL 搜索真实有效**：字节/美团/腾讯/知乎 + Moka/飞书系
- ❌ **其余公司 URL 搜索无效**，需要进主页用站内搜索

**给用户的使用建议**：
1. **优先用字节/美团/腾讯/知乎的链接**（URL 搜索真实有效）
2. **其余公司**：进首页 → 站内搜方向词 → 选"职位类别"过滤
3. **不要相信一个看起来正常的 URL 真的过滤了关键词**——很多公司的 URL 参数被忽略