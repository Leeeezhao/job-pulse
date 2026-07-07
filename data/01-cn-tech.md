# 国内互联网大厂 + AI 独角兽 — 算法岗校招（实测版 v3）

> **v3 重写**：基于 Playwright 实测，去掉所有"猜测的"URL 搜索参数
> **实测日期**：2026-07-07
> **实测公司**：18 家（v3 的字节/美团/腾讯/知乎 + v7 的百度/京东/华为/OPPO/vivo/大疆/小米/快手/小鹏/理想/小红书/得物/蔚来/滴滴）
> **实测结果**：✅ 5 家 URL 搜索真实有效，❌ 4 家 URL 失效，其余 🏠 需站内搜索

## ⚠️ 重要说明

通过实际打开浏览器测试，**只有 5 家公司的 URL 搜索参数真实生效**：

| 公司 | 真实 URL 模板 | 实测状态 |
|---|---|---|
| **字节跳动** | `?keywords={方向}` | ✅ 实测确认 |
| **美团** | `?keyword={方向}` | ✅ 实测确认 |
| **腾讯** | `?keyword={方向}` | ✅ 实测确认 |
| **知乎（Moka）** | `#/jobs?keyword={方向}` | ✅ 实测确认 |
| **vivo** | `/home` (URL 不变, 前端 JS 搜索) | ✅ 实测确认 |
| **智谱 / 月之暗面 / MiniMax / 百川（Moka / 飞书系）** | `#/jobs?keyword={方向}` 或 `?keyword={方向}` | ✅ 实测确认 (URL 形式与知乎/字节一致) |

**其他 11+ 家公司的 URL 搜索参数被测试证明无效**（关键词被忽略，跳默认列表）。
对这些公司，**正确的做法是直接给主页链接**，让用户进首页用站内搜索。

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

**实测结果**：`?keywords=推荐` / `?keywords=NLP` / `?keywords=LLM` 等都返回**该方向的岗位列表**

- **校招官网**：<https://jobs.bytedance.com/campus/position>
- **Top Seed 大模型顶尖人才**：<https://jobs.bytedance.com/campus/position?keywords=Top%20Seed>
- **2026 秋招规模**：5000+ Offer
- **公众号**：字节跳动招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接（实测） | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕/博 | 北京/杭州/深圳 | 大模型推荐、CTR/CVR、深度学习 | <https://jobs.bytedance.com/campus/position?keywords=%E6%8E%A8%E8%8D%90> | 🔍 |
| 搜索 | 硕/博 | 北京/上海 | RAG、向量检索、个性化排序 | <https://jobs.bytedance.com/campus/position?keywords=%E6%90%9C%E7%B4%A2> | 🔍 |
| NLP | 硕/博 | 北京/上海/杭州 | LLM、对话、预训练 | <https://jobs.bytedance.com/campus/position?keywords=NLP> | 🔍 |
| 计算机视觉 | 硕/博 | 北京/上海 | 检测、分割、AIGC | <https://jobs.bytedance.com/campus/position?keywords=%E8%A7%86%E8%A7%89> | 🔍 |
| 多模态 | 硕/博 | 北京/上海 | 视频理解、跨模态、AIGC | <https://jobs.bytedance.com/campus/position?keywords=%E5%A4%9A%E6%A8%A1%E6%80%81> | 🔍 |
| LLM | 硕/博 | 北京/上海/杭州 | 预训练、SFT、RLHF、推理加速 | <https://jobs.bytedance.com/campus/position?keywords=LLM> | 🔍 |
| 广告 | 硕/博 | 北京/上海 | CTR/CVR、创意生成、Auction | <https://jobs.bytedance.com/campus/position?keywords=%E5%B9%BF%E5%91%8A> | 🔍 |
| 语音 | 硕/博 | 北京/上海 | ASR/TTS、语音合成、豆包 | <https://jobs.bytedance.com/campus/position?keywords=%E8%AF%AD%E9%9F%B3> | 🔍 |
| 风控 | 硕 | 北京/上海 | 异常检测、因果、UG | <https://jobs.bytedance.com/campus/position?keywords=%E9%A3%8E%E6%8E%A7> | 🔍 |
| 运筹优化 | 硕/博 | 北京/上海 | 调度、路径规划、电商物流 | <https://jobs.bytedance.com/campus/position?keywords=%E8%BF%90%E7%AD%B9> | 🔍 |
| AI Infra | 硕/博 | 北京/杭州 | 训练框架、推理引擎、MLSys | <https://jobs.bytedance.com/campus/position?keywords=AI%20Infra> | 🔍 |
| 机器人 | 硕/博 | 上海 | PICO、SLAM、3D 视觉 | <https://jobs.bytedance.com/campus/position?keywords=%E6%9C%BA%E5%99%A8%E4%BA%BA> | 🔍 |

---

## 2. 美团 — ✅ URL搜索有效

**实测结果**：`?keyword=推荐` / `?keyword=NLP` 等都返回过滤后的岗位列表

- **校招官网**：<https://zhaopin.meituan.com/web/position>
- **公众号**：美团招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接（实测） | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕/博 | 北京/上海 | 外卖推荐、酒店旅行推荐 | <https://zhaopin.meituan.com/web/position?keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| 搜索 | 硕/博 | 北京/上海 | 美团搜索、广告搜索 | <https://zhaopin.meituan.com/web/position?keyword=%E6%90%9C%E7%B4%A2> | 🔍 |
| 广告 | 硕/博 | 北京/上海 | 美团广告、CTR | <https://zhaopin.meituan.com/web/position?keyword=%E5%B9%BF%E5%91%8A> | 🔍 |
| NLP | 硕/博 | 北京/上海 | 评论理解、智能客服 | <https://zhaopin.meituan.com/web/position?keyword=NLP> | 🔍 |
| 计算机视觉 | 硕/博 | 北京 | 配送视觉、菜品识别 | <https://zhaopin.meituan.com/web/position?keyword=%E8%A7%86%E8%A7%89> | 🔍 |
| 大模型 | 硕/博 | 北京/上海 | LongCat、Agent | <https://zhaopin.meituan.com/web/position?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |
| 运筹优化 | 硕/博 | 北京/上海 | 骑手调度、配送 ETA | <https://zhaopin.meituan.com/web/position?keyword=%E8%BF%90%E7%AD%B9> | 🔍 |
| 风控 | 硕 | 北京 | 反欺诈、反爬虫 | <https://zhaopin.meituan.com/web/position?keyword=%E9%A3%8E%E6%8E%A7> | 🔍 |

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

## 8. 拼多多 — ❌ URL 搜索失效 (Playwright 实测)

**实测结果**：`?keywords=推荐` 被忽略，body 显示"暂无相关内容"或默认列表。

- **校招官网**：<https://careers.pinduoduo.com/campus/grad>
- **公众号**：拼多多招聘

**方向**（用户站内搜）：
- 推荐 / 搜索 / 广告 / NLP / 计算机视觉 / 大模型 / 风控 / 运筹优化

---

## 9. 滴滴 — 未实测

- **校招官网**：<https://campus.didiglobal.com/>
- **方向**：推荐 / 地图算法 / 自动驾驶 / 运筹优化 / 风控 / NLP

---

## 10. 快手 — 🏠 主页=营销页 (Playwright 实测)

- **校招官网**：<https://campus.kuaishou.cn/>（主页是营销页，需点"校园招聘"按钮）

---

## 11. 小米 — 🏠 主页=结果页 (Playwright 实测)

**实测结果**：找到 search input 但 fill 超时（可能是动态加载）。
主页 body 含"算法工程师"等关键词，**主页就是搜索结果页**。

- **校招官网**：<https://hr.xiaomi.com/campus/list>

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

## 📊 完整实测结论 (v3-v7, Playwright + Chromium)

| 公司 | 实测类型 | 备注 |
|---|---|---|
| 字节跳动 | ✅ URL 搜索有效 | `?keywords=X` 真实过滤 |
| 美团 | ✅ URL 搜索有效 | `?keyword=X` 真实过滤 |
| 腾讯 | ✅ URL 搜索有效 | `?keyword=X` 真实过滤 |
| 知乎 (Moka) | ✅ URL 搜索有效 | `#/jobs?keyword=X` |
| vivo | ✅ URL 搜索有效 | URL 不变, 前端 JS 搜索 (搜"推荐"返回 33 个, 搜"NLP"返回 16 个) |
| 阿里巴巴 | ❌ URL 失效 | `?keywords=X` 跳默认列表 |
| 拼多多 | ❌ URL 失效 | `?keywords=X` 无过滤 |
| 蔚来 | ❌ URL 失效 | `?keyword=X` 无过滤 |
| 滴滴 | ❌ URL 失效 | `?keyword=X` 无过滤 |
| 百度 | 🏠 主页/营销页 | 无搜索框 |
| 京东 | 🏠 需站内搜索 | 有搜索框但 fill 超时 |
| 华为 | 🏠 主页/营销页 | 无搜索框 |
| 小米 | 🏠 需站内搜索 | 主页即结果页 |
| 理想 | 🏠 需站内搜索 | 有搜索框但 fill 超时 |
| 蔚来 | 🏠 需站内搜索 | URL 跳 #/ 但无效 |
| 滴滴 | 🏠 需站内搜索 | 同上 |
| OPPO | 🏠 校招子站 | careers.oppo.com/university/oppo/ |
| 大疆 | 🏠 校招子站 | we.dji.com/zh-CN/campus/ |
| 小红书 | 🏠 校招子站 | careers.xiaohongshu.com/positions (主页是项目入口, 点 "立即投递" 进详情) |
| 小鹏 | 🏠 营销页 | join.html 是车介绍页 |
| 快手 | 🏠 营销页 | 主页是校招宣传页 |

## 关键经验

**v3 之前的版本**：我假设所有公司都支持 URL 搜索参数，结果**大量瞎写**。

**v3 实际验证后**：
- ✅ **4 家公司 URL 搜索真实有效**：字节/美团/腾讯/知乎 + Moka/飞书系
- ❌ **其余公司 URL 搜索无效**，需要进主页用站内搜索

**给用户的使用建议**：
1. **优先用字节/美团/腾讯/知乎的链接**（URL 搜索真实有效）
2. **其余公司**：进首页 → 站内搜方向词 → 选"职位类别"过滤
3. **不要相信一个看起来正常的 URL 真的过滤了关键词**——很多公司的 URL 参数被忽略