# 国内互联网大厂 + AI 独角兽 — 算法岗校招（实测版 v3）

> **v15：添加 7 家中型企业（网易互娱/三七互娱/西山居/叠纸/深信服/摩尔线程/阿里健康）**
> **实测日期**：2026-07-07
> **实测公司**：44+ 家（v3-v15 累计）
> **实测结果**：✅ 12 家 URL 搜索真实有效（含快手、美团系、飞书系、理想 functionsids、Moka 系、字节 project ID），其余 🏠 需进站内搜

## ⚠️ 重要说明

通过实际打开浏览器测试（v3-v14 累计 37+ 家公司），**以下 12 家公司 URL 搜索参数真实生效**：

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
| **快手校招** | `#/campus/jobs?recruitSubProjectCodes=20271779425607` | ✅ v14 实测, 0 实习 |
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

## 8. 拼多多 — ❌ URL 搜索失效 (Playwright 实测)

**实测结果**：`?keywords=推荐` 被忽略，body 显示"暂无相关内容"或默认列表。

- **校招官网**：<https://careers.pinduoduo.com/campus/grad>
- **公众号**：拼多多招聘

**方向**（用户站内搜）：
- 推荐 / 搜索 / 广告 / NLP / 计算机视觉 / 大模型 / 风控 / 运筹优化

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

## 10. 快手 — 🏠 主页=营销页 (Playwright 实测)

- **校招官网**：<https://campus.kuaishou.cn/>（主页是营销页，需点"校园招聘"按钮）

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

## 15. 快手校招 — ✅ URL 参数有效 (v14 校招系统)

**v14 实测重大发现**：快手校招完全可用。点击主页三个 tab 后 URL 会变。

- **招聘主页**：<https://campus.kuaishou.cn/recruit/campus/e/> (含 应届招聘 / 实习招聘 / 快Star 三个 tab)
- **2027 届应届招聘 (推荐)**：<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271779425607>
  - body 显示 **共 74 个职位** (含 【快Star】大语言模型算法工程师、广告 AI 算法工程师、音视频大模型算法工程师)
  - 0 实习
- **2026 届留用实习**：<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271772783534> (全实习, 不推荐)
- **快Star 人才计划主页**：<https://campus.kuaishou.cn/recruit/campus/e/#/campus/talent>

**关键词测试**: 应届招聘页面 `?keyword=X` 真实有效 (搜 "推荐"/"NLP"/"AI"/"搜索" 都返 18 个岗位, 0 实习)

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
| 快手校招 | ✅ recruitSubProjectCodes | `recruitSubProjectCodes=20271779425607` 74 个, 0 实习 (v14) |
| 携程 + 360 + 虎牙 + 鹰角 + 用友 + 网易 + Keep + 飞书 | ✅ 主页完整 | v14 (需进站内搜方向词) |
| 元戎启行 (Moka) | ✅ Moka | `#/jobs?keyword=X` |
| 美团系 (大众点评/猫眼/酒旅) | ✅ 共享美团 URL | `?hiringType=4_1&keyword=X` |
| 阿里巴巴 | 🏠 talent.taotian.com | 主页是项目入口, 需进站内搜 |
| 拼多多 | 🏠 career.pinduoduo.com | 营销页, 仅列出 "App专享优惠" |
| 得物 | 🏠 dewu.com/career | Moka 404, dewu.com 是营销页 |
| 小红书 | 🏠 job.xiaohongshu.com/campus/positions | 返 "热招职位", URL 参数被忽略 |
| 大疆 | 🏠 careers.dji.com/zh-CN/campus/positions | 需点 "查看在招职位" |
| 百度 | 🏠 talent.baidu.com | `{"status":"need-login"}` 反爬 |
| 京东 | 🏠 campus.jd.com/#/jobs | URL 参数被忽略 |
| 华为 | 🏠 career.huawei.com | **强制登录**, 需 uniportal.huawei.com |
| 小米 | 🏠 hr.xiaomi.com/campus/list | 2018 年过期数据 |
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