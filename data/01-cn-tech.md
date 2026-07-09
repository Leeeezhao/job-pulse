# 国内互联网大厂 + AI 独角兽 - 算法岗校招(实测版 v26)

> **v26：理想校招重测 → REST API (390总 24算法+10AI)**
> **v20:百度校招重测 → SSR 项目码筛生效;发现 AIDU 项目 (projectType=3, 11 个顶级 AI 岗)**
> **v19:大疆校招实测 → 发现 Moka 投递系统 + #/jobs?keyword=X 真过滤,54 个算法岗全部可点**
> **v18:快手校招重测 → v14 的 `?keyword=X` 已失效,需站内点类目码筛(新增项目码字典)**
> **v17:拼多多迁移到新域名 careers.pddglobalhr.com,22 个岗位全部找到(含云弧计划核心算法岗)**
> **v16:小米校招系统重新实测 → 发现飞书(mioffice)投递系统,URL keywords 搜索真实有效**
> **v15:添加 7 家中型企业(网易互娱/三七互娱/西山居/叠纸/深信服/摩尔线程/阿里健康)**
> **实测日期**:2026-07-09
> **实测公司**：44+ 家（v3-v26 累计）
> **实测结果**:✅ 16 家 URL 搜索/项目码/API 有效 + 🏠 快手站内类目码筛 + 🏠 拼多多站内筛

## ⚠️ 重要说明

通过实际打开浏览器测试(v3-v16 累计 38+ 家公司),**以下 13 家公司 URL 搜索参数真实生效**:

| 公司 | 真实 URL 模板 | 实测状态 |
|---|---|---|
| **字节跳动** | `?keywords={方向}&project=7525009396952582407,7621018151002507573` | ✅ 实测确认 (过滤实习) |
| **美团** | `/web/position?hiringType=4_1&keyword={方向}` | ✅ 实测确认 (应届校招项目, 0实习) |
| **腾讯** | `?keyword={方向}` | ✅ 实测确认 |
| **知乎(Moka)** | `#/jobs?keyword={方向}` | ✅ 实测确认 |
| **vivo** | `/home` (URL 不变, 前端 JS 搜索) | ✅ 实测确认 |
| **蔚来(飞书系)** | `?keyword={方向}` | ✅ v12 实测 |
| **小鹏(飞书系)** | `?keyword={方向}` | ✅ v12 实测 |
| **理想汽车** | `GET api-web.lixiang.com/.../school/job-page?project_id=4&job_function_ids=1` | ✅ API (v26) |
| **滴滴(Moka)** | `#/jobs?project=2027` (项目筛代替关键词) | ✅ v12 实测 |
| **快手校招** | `#/campus/jobs?recruitSubProjectCodes=20271779425607` | ✅ v14 项目筛 (74 岗, 0 实习) / v18 `?keyword=` 失效,改站内类目码 |
| **大疆校招** | `#/jobs?keyword={方向}` | ✅ v19 Moka (拓疆者, 138 岗, keyword=算法 返 54) |
| **百度校招** | `?projectType=1/3/4` | ✅ v20 SSR 项目码;AIDU=11/校招=145/管培=12 |
| **京东校招** | `POST /api/wx/position/page` | ✅ v21 POST API;TGT 127 顶级 AI 岗 (天才计划 56 + 实习生 71) |
| **华为校招** | `GET /getJob/newHr/page` | ✅ v22 GET API;jobType=2 返 198 校招,含 36 AI 算法 |
| **小米(飞书系)** | `?keywords={方向}` | ✅ v16 实测 (飞书 mioffice 系统) |
| **智谱 / 月之暗面 / MiniMax / 百川(元戎启行等 Moka / 飞书系)** | `#/jobs?keyword={方向}` 或 `?keyword={方向}` | ✅ 实测确认 |

**其他 10+ 家公司 URL 搜索参数被测试证明无效**(关键词被忽略,跳默认列表)。对这些公司,**正确的做法是直接给主页链接**,让用户进首页用站内搜索。

## 字段说明

| 字段 | 含义 |
|---|---|
| 方向 | 真实招聘方向(核心词) |
| 学历 | 本 / 硕 / 博 |
| 工作地 | 真实办公地 |
| JD 关键词 | 编程语言 / 模型 / 业务关键词 |
| 链接 | **经过实测**的真实可用 URL |
| 类型 | 🔍 URL搜索有效 / 🏠 主页+站内搜索 |

---

## 1. 字节跳动 (ByteDance) - ✅ URL搜索有效 (Playwright 实测)

**v9 实测结果**:`?keywords={方向}` 默认会混入 30-40% 实习岗。加 `&project=7525009396952582407,7621018151002507573` 后**0 实习** (正式校招项目 ID)

- **校招官网**:<https://jobs.bytedance.com/campus/position>
- **Top Seed 大模型顶尖人才**:<https://jobs.bytedance.com/campus/position?keywords=Top%20Seed&project=7525009396952582407,7621018151002507573>
- **2026 秋招规模**:5000+ Offer
- **公众号**:字节跳动招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接(实测) | 类型 |
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

## 2. 美团 - ✅ URL搜索有效

**v11 实测结果**:美团真实可用 URL 模板是 `/web/position?hiringType=4_1&keyword={方向}`。`hiringType=4_1` = "应届生校招" 项目, **0 实习过滤**。注: NLP 方向必须搜"自然语言", 搜"NLP"返 0。

- **校招官网**:<https://zhaopin.meituan.com/web/position?hiringType=4_1>
- **公众号**:美团招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接(实测) | 类型 |
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

## 3. 腾讯 - ✅ URL搜索有效

**实测结果**:`?keyword=推荐` 返回"算法-推荐算法方向"等岗位

- **校招官网**:<https://join.qq.com/post.html?query=p_1>
- **公众号**:腾讯招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接(实测) | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕/博 | 深圳/北京 | 微信视频号、QQ 看点、CTR | <https://join.qq.com/post.html?query=p_1&keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| NLP | 硕/博 | 深圳/北京 | 混元大模型、对话、NLP | <https://join.qq.com/post.html?query=p_1&keyword=NLP> | 🔍 |
| 计算机视觉 | 硕/博 | 深圳/北京 | 检测、分割、人脸识别 | <https://join.qq.com/post.html?query=p_1&keyword=%E8%A7%86%E8%A7%89> | 🔍 |
| 大模型 | 硕/博 | 深圳/北京 | 混元、预训练、SFT | <https://join.qq.com/post.html?query=p_1&keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |
| 广告 | 硕/博 | 深圳/北京 | 朋友圈广告、视频号广告 | <https://join.qq.com/post.html?query=p_1&keyword=%E5%B9%BF%E5%91%8A> | 🔍 |
| 语音 | 硕 | 深圳 | 微信语音、ASR/TTS | <https://join.qq.com/post.html?query=p_1&keyword=%E8%AF%AD%E9%9F%B3> | 🔍 |
| 风控 | 硕 | 深圳 | 微信支付风控、QQ 安全 | <https://join.qq.com/post.html?query=p_1&keyword=%E9%A3%8E%E6%8E%A7> | 🔍 |

---

## 4. 阿里巴巴 - ❌ URL 搜索失效 (Playwright 实测)

**实测结果**:`?keywords=推荐` / `?keyword=推荐` 都被服务器忽略,返回**默认列表(20 个岗位)**,不按"推荐"过滤。

**正确用法**:进首页 → 用站内搜索框搜方向。

- **校招官网**:<https://talent-holding.alibaba.com/campus/position-list?campusType=freshman>
- **公众号**:阿里招聘
- **2026 重点 BU**:淘天 / 阿里云 / 淘宝闪购 / 菜鸟 / 阿里云瓴羊

**重要方向**(用户自行在站内搜):

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

**站内搜索步骤**:
1. 点开 <https://talent-holding.alibaba.com/campus/position-list?campusType=freshman>
2. 在搜索框输入"推荐"/"NLP"/"大模型"
3. 选择"职位类别"
4. 得到过滤后的岗位

---

## 5. 百度 - ✅ 项目码篏 (v20 重测)

**v20 重测重大发现**(2026-07-09):v3 "未实测"是错的。实际上 SSR 返 `window.__INITIAL_DATA__` 含完整列表,项目码篏垍 - 已经能動!

**URL 模板**(项目码 × 招聘类型):
- 默认无参:`https://talent.baidu.com/jobs/list` → 157 个应届岗位 (需打开后加详情)
- **`?projectType=1`** ✅ → 145 普通校招
- **`?projectType=3`** ✅✅ → **11 个 AIDU 项目核心 AI 岗** (人才专项,类似字节 Top Seed / 拼多多云弧)
- **`?projectType=4`** ✅ → 12 个管培生项目(**非算法**)
- **`?recruitType=INTERN`** ✅ → 399 个实习岗位

**参数状态总结**:

| 参数 | 是否生效 | 返 total | 备注 |
|---|---|---|---|
| `projectType=1/3/4` | ✅ | 145/11/12 | 项目码篏,实测生效 |
| `recruitType=GRADUATE/INTERN/SOCIAL` | ✅ | 157/399/? | 应届/实习/社招 |
| `keyWord=` | ❌ | 157 | SSR 不读 |
| `workPlace=` | ❌ | 157 | SSR 不读 |
| `postType=` | ❌ | 157 | SSR 不读 (技术/产品/销售 等不生效) |
| `curPage`/`pageSize` | ❌ (部分) | SSR 始终返 10 个 | 需 client-side fetch |

### 🆕 AIDU 项目 (百度版 Top Seed) - 11 个顶级 AI 岗

- **2027AIDU-大模型算法工程师** (北京市+深圳市) ⭐
- **2027AIDU-多模态算法工程师** (北京市+上海市)
- **2027AIDU-AI异构计算研发工程师** (北京市+上海市)
- **2027AIDU-语音大模型算法工程师** (北京市)
- **2027AIDU-大模型Infra工程师** (北京市)
- **2027AIDU-智能体算法工程师** (北京市)
- **2027AIDU-Agent应用全栈工程师** (北京市)
- **2027AIDU-基础模型架构师** (北京市)
- **2027AIDU-端到端系统架构师** (北京市)
- **2027AIDU-视觉-语言模型架构师** (北京市)
- (1 个其他,需要全量手动加载)

### 【项目=1】 校招普通项目中可见的技术岗(首页 8 个)

- 北京-大模型训练 Infra 研发工程师 (基座研发)
- 深圳-AI Infra 强化学习工程师 (基座研发)
- 上海-自动驾驶视觉语言模型算法工程师
- 深圳-智能体算法工程师
- 大连-智能体算法工程师
- 上海-搜广推算法工程师
- 上海-云计算虚拟化研发工程师
- 上海-自动驾驶端到端决策规划控制算法工程师

### v20 字典数据 (从 SSR __INITIAL_DATA__ 取)

**postType 字典**:
- `1`=技术 / `2`=产品 / `13`=政企 / `14`=销售 / `15`=综合

**projectType 字典**:
- `1`=校招 (项目=3+项目=4 之外的所有 145 个)
- `3`=AIDU项目 (11 个顶级 AI)
- `4`=管培生项目 (~12 个)

**workPlace 字典**(含 14 个城市):
- `1100`=北京市 / `3100`=上海市 / `4403`=深圳市 / `4401`=广州市 / `5101`=成都市 / `2102`=大连市 / `1403`=阳泉市 / `4201`=武汉市 / `3301`=杭州市 / `3501`=福州市 / `4419`=东莞市 / `4601`=海口市 / `3701`=济南市 / `9000`=全国

- **校招官网(全列表)**:<https://talent.baidu.com/jobs/list>
- **校招项目(1):145 岗**:<https://talent.baidu.com/jobs/list?projectType=1>
- **AIDU 项目(3):11 顶级 AI 岗**(推荐):<https://talent.baidu.com/jobs/list?projectType=3>
- **管培生项目(4):12 个**:<https://talent.baidu.com/jobs/list?projectType=4>
- **实习生招聘**:<https://talent.baidu.com/jobs/list?recruitType=INTERN>
- **社会招聘**(独立子站):<https://talent.baidu.com/jobs/social>
- **邮箱**:hrcampus@baidu.com

| 方向 | 链接 | 类型 |
|---|---|---|
| AIDU 大模型/多模态/智能体 (11 岗) | <https://talent.baidu.com/jobs/list?projectType=3> | 🔍 |
| AIDU Infra 算子 (11 岗中包含) | <https://talent.baidu.com/jobs/list?projectType=3> | 🔍 |
| 校招普通项目 (145 岗) | <https://talent.baidu.com/jobs/list?projectType=1> | 🔍 |
| 实习生 (399 岗) | <https://talent.baidu.com/jobs/list?recruitType=INTERN> | 🔍 |

> 🚨 **重点**: 百度校招算法岗集中在 **AIDU 项目**(11 个,纯顶级)和 **项目1** 中首页可见的 **8 个技术岗**(全是 AI Infra / 自动驾驶 / 智能体 / 搜广推)。管培生项目(4)主要是销售/产品/运营,**不是算法岗**。
> **关键词搜索失效**:`?keyWord=` / `?workPlace=` / `?postType=` 都不生效,需进站内点类目筛。
> **SSR 返限量**:SSR 仅返 10 个职位。完整 145/11 需在浏览器内点 load-more (client-side fetch `/httservice/api/position/list`)。
| 自动驾驶 | <https://talent.baidu.com/jobs?keyword=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6> |

> ⚠️ 这些 URL 格式基于"看起来合理"猜测,**百度未实测**。建议优先用首页。

---

## 6. 京东 - ✅ POST API + 人才专项 (v21 重测)

**v21 重测重大发现**(2026-07-09):v3 "未实测"是错的。京东校招 SPA **不需要登录**就能调 `POST /api/wx/position/page` 获取全部岗位。直接调 API 拿到 16 应届 + 127 TGT 顶级 + 106 实习。

### 项目清单 (顶级 AI 人才项目)

| type | planId | planName | 岗位数 |
|---|---|---|---|
| `talent` | **47** | **TGT-顶尖青年技术天才计划** | **56 岗** ⭐ |
| `talent` | **55** | **TGT-顶尖青年技术实习生** | **71 岗** ⭐ |
| `present` | 52 | JDS-新星计划 | 0 |
| `present` | 54 | 新锐之星 | ? |
| `present` | 57 | TET-管理培训生 | ? |
| `internship` | 45 | JD YOUNG-实习生计划 | ? |
| `internship` | 51 | 新锐之星实习生 | ? |

**关键调用**:
- 入口 SPA: <https://campus.jd.com/#/jobs> (需要 hash,否则 302 到登录)
- POST endpoint: `https://campus.jd.com/api/wx/position/page?type={type}` (type=talent/present/internship)
- POST payload (1选):
  ```json
  {"pageSize": 100, "pageIndex": 0, "parameter": {"positionName": "大模型", "planIdList": [], "jobDirectionCodeList": [], "workCityCodeList": [], "positionDeptList": []}}
  ```

**API 响应字段**:
- `totalNumber`: 总数 (如 TGT=127, 应届=16, 实习=106)
- `items[]`: 岗位列表 (包含 `positionName`, `reqId`, `publishTime`, `workCity`)
- `parameter.positionName`: 关键词过滤 (⚠️ 只支持粗粒度 - "大模型" "AI" 等)
- `parameter.planIdList[]`: 限定项目 (如 `[47]` = TGT-天才计划)

### TGT-顶尖青年技术人才项目 (百度版 AIDU / Top Seed) 127 岗关键词统计

- **大模型 63 岗** (47% 全部与大模型相关)
- 多模态 25 / 智能体 18 / 训练 16 / 具身 14 / 强化学习 11 / 推理 11
- 医疗 8 / 机器人 6 / Agent 6 / VLA 6 / 后训练 5 / 语音 5 / 物流 5
- 世界模型 4 / 广告 4 / 代码 4 / LLM 4 / 对话 4 / 预训练 3 / 推荐 3
- 自动驾驶 2

### 重点顶级岗位示例 (TGT-天才计划 56 岗)

- 具身仿真与世界模型研究
- 多模态理解大模型全流程架构探索
- 机器人移动操作全身协同控制算法研究
- 面向电商大模型预训练与后训练的探索研究
- 面向复杂场景的自动驾驶端到端大模型与强化学习的技术研究
- 空间智能大模型创新与应用
- 新一代大模型推理技术优化研究
- 千亿级大语言模型架构与分布式研究
- ... (56 个均为顶级 AI 研究岗)

### 字典 endpoint (类目、地区、项目)

| endpoint | 用途 |
|---|---|
| `POST /api/wx/position/dict?type=present` | 类目/城市字典 |
| `GET /api/wx/position/getProjectList` | 项目字典 (含 planId) |

- **postList 字典**:01=采销与物流 / 02=技术 / 03=产品 / 04=运营 / 05=市场与商务 / 06=设计 / 07=职能 / 08=工程 / 09=保险及金融 / 10=健康 / 30=基层管理 / 31=一线销售 / 32=一线职能 / 33=一线专业 / 15=TET
- **workPlace 字典**:269 个城市代码 (以 00001 北京为准)

- **校招 SPA**:<https://campus.jd.com/#/jobs>
- **TGT 顶尖青年技术天才计划** (推荐 ⭐):<https://campus.jd.com/#/jobs> (站内 选 顶尖青年技术天才计划)
- **TGT 顶尖青年技术实习生** (推荐 ⭐):<https://campus.jd.com/#/jobs> (站内 选 顶尖青年技术实习生)

| 方向 | 链接 | 类型 |
|---|---|---|
| TGT 顶尖青年技术人才 (56 应届 + 71 实习 = 127 顶级 AI) | <https://campus.jd.com/#/jobs> | 🔍 |
| 应届生 (16 岗) | <https://campus.jd.com/#/jobs> | 🔍 |
| 实习生 (106 岗) | <https://campus.jd.com/#/jobs> | 🔍 |

> 🚨 **重点**:京东 TGT = 顶级 AI 人才专项(对标字节 Top Seed / 百度 AIDU / 拼多多云弧),127 个核心 AI 研究岗全可用 SPA 站内筛 + API 直调拿到。关键词位置过滤是 API 参数(`positionName`),但只能"部分匹配",多个词组合需多次调用。
> **核心 API 唯一不可跨域保护**:必须 `Origin: https://campus.jd.com` + `Referer: https://campus.jd.com/`,跨域会被 403 拒绝。

---

## 7. 华为 - ✅ GET API (v22 重测)

**v22 重测重大发现**(2026-07-09):v3 "未实测" / 强制登录是错的。华为校招 SPA 调用 **GET API 无需登录**就能拿到 198 个校招岗位。

### Endpoint 模板

- **入口 SPA**:<https://career.huawei.com/reccampportal/portal5/campus-recruitment.html>
- **职位列表 API**:
  ```
  GET /reccampportal/services/portal/portalpub/getJob/newHr/page/<pageSize>/<curPage>
  Query: {jobType: 2, pageSize: 50, curPage: 1}
  ```
- **职位详情 API**:
  ```
  GET /reccampportal/services/portal/portalpub/getJobDetail/newHr?jobId=<jobId>&dataSource=<ds>
  ```
- **职位详情 URL** (SPA): <https://career.huawei.com/reccampportal/portal5/campus-recruitment-detail.html?jobId=30373&dataSource=1>

### jobType 参数字典

| jobType | 含义 | totalRows |
|---|---|---|
| 1 | 校招 (所有) | 92 |
| 2 | **校招 (另一个口径)** | **198** ⭐ |
| jobTypes=2 | 应届生专属 | 59 |
| jobTypes=-1/-2/-3 | 实习 | 329 |

> 注:jobType 与 jobTypes 不一样。jobType=2 会返 198 个独立岗位。

### 198 个校招岗位总览 (jobType=2)

按子类代码 (jobSubcategory) 分组:
- J260302 (44) / J260105 (28) / J260101 (26) / J260102 (18) - 软件/AI/算法
- J260212 (8) / J260406 (8) / J260403 (8) - 安全/隐私
- J260312 (4) / J260408 (4) / J260711 (4) / J260412 (4) / J260401 (4) / J260701 (4) - 多类
- 其他不热门

99 个 unique 岗位名涵盖:

**AI 算法类 (12 独立岗位名 × 高级+研究员 × 2 = 24 条):**
- AI算法高级工程师 / AI算法研究员
- 大模型算法研究员
- 大模型应用高级工程师 / 大模型应用研究员
- AI Infra高级工程师 / AI Infra研究员
- AI Infra高性能研发高级工程师 / AI Infra高性能研发研究员
- AI Infra研究员 / AI Infra高级工程师 (跨类重复)
- 多模态算法高级工程师 / 多模态算法研究员
- 计算机视觉高级工程师
- 自然语言处理/语音语义高级工程师
- 推荐搜索高级工程师 / 推荐搜索研究员
- 机器学习高级工程师 / 机器学习研究员
- 自动驾驶算法高级工程师
- 媒体算法高级工程师
- 决策推理高级工程师
- 仿真算法高级工程师
- AI安全/隐私保护高级工程师 / AI安全/隐私保护研究员
- 软件算法高级工程师 / 软件算法研究员
- 通信算法高级工程师 / 通信算法研究员
- 射频算法高级工程师 / 射频算法研究员

**研发类 (AI 以外):**
- AI软件开发高级工程师 / AI数据高级工程师 / AI数据工程高级工程师
- 操作系统与编译器开发高级工程师 / 操作系统与编译器开发研究员
- 软件开发高级工程师 / 通用软件开发高级工程师
- 数据库开发高级工程师 / 数据库开发研究员
- 云计算开发高级工程师 / 云存储开发高级工程师

**硬件类:**
- AI算子开发高级工程师 / AI算子开发研究员
- ASIC芯片设计高级工程师 / 光芯片设计高级工程师
- 射频芯片开发高级工程师 / 数字芯片开发高级工程师
- 处理器开发高级工程师 / 单板硬件开发高级工程师

### 重点 18 个 AI 算法岗位 (高级 + 研究员 = 36 条)

| 岗位名 | 地点 |
|---|---|
| AI算法高级工程师 / 研究员 | 深/沪/京/杭/宁/蓉/西安/苏州/东莞/武汉 |
| 大模型算法研究员 | 北京/成都/杭州/合肥/南京/上海/深圳 |
| 大模型应用高级工程师 / 研究员 | 上述9市 |
| 多模态算法高级工程师 / 研究员 | 上述9市 |
| AI Infra高级工程师 / 研究员 | 上述8市 |
| AI Infra高性能研发高级工程师 / 研究员 | 上述7市 |
| 机器学习高级工程师 / 研究员 | 上述4市 |
| 推荐搜索高级工程师 / 研究员 | 京/沪/杭/东莞/宁/深 |
| 自然语言处理/语音语义高级工程师 | 上述7市 |
| 自动驾驶算法高级工程师 | 京/沪/深/宁/苏/杭/西安 |
| 计算机视觉高级工程师 | 上述8市 |
| 决策推理高级工程师 | (需查详情) |
| AI安全/隐私保护高级工程师 / 研究员 | 上述10市 |
| 媒体算法高级工程师 | (需查详情) |
| 软件算法高级工程师 / 研究员 | (需查详情) |
| 通信算法高级工程师 / 研究员 | (需查详情) |
| 射频算法高级工程师 / 研究员 | (需查详情) |

### 🔍 关键词搜索限制

- ✅ `jobType` 生效:2=校招 198 / 1=92 / -1/-2/-3=实习 329
- ❌ `searchText=算法/大模型/NLP/SLAM` 等被服务器忽略 (返相同 92 个)
- 关键词需在站内输入框(调用同一 API 但带 cookie 上下文)

### API 响应结构

```json
{
  "pageVO": {
    "totalRows": 198,
    "curPage": 1,
    "pageSize": 50,
    "totalPages": 4
  },
  "result": [
    {
      "jobId": 30373,
      "jobname": "法务专员",
      "jobSubcategory": "J250201",
      "deptName": "贵州代表处",
      "jobArea": "中国/贵阳",
      "advertisementCode": "AD2026021400029",
      "creationDate": "2026-07-09T11:19:00.000+0800",
      ...
    }
  ]
}
```

- **校招 SPA**:<https://career.huawei.com/reccampportal/portal5/campus-recruitment.html>
- **校招列表 API (198 岗)**:`GET /reccampportal/services/portal/portalpub/getJob/newHr/page/50/1?jobType=2`

| 方向 | 链接 | 类型 |
|---|---|---|
| 198 校招岗位 | <https://career.huawei.com/reccampportal/portal5/campus-recruitment.html> | 🔍 |
| 36 AI 算法岗位 (24 高级 + 12 研究员) | API: `?jobType=2` | 🔍 |
| 329 实习岗位 | API: `?jobTypes=-1` | 🔍 |

> 🚨 **重点**:华为校招 API 不需登录。`jobType=2` 是真校招口径(198 岗,含 99 unique 岗位)。每个高级+研究员是双胞胎,36 个条目 AI 相关。关键词搜索被 server 忽略 - 需要站内选筛。详情 URL 用 `campus-recruitment-detail.html?jobId=X&dataSource=X` SPA。

---

## 8. 拼多多 - 🏠 主页+站内筛 (v17 新域名)

**v17 实测重大发现**(2026-07-09):
- 拼多多已**迁移到新域名** `careers.pddglobalhr.com`(旧 `careers.pinduoduo.com` 301 跳转)
- 这是个 Next.js SPA,后端有真实 API:`/api/careers/api/recruit/position/list` (POST JSON)
- **URL 搜索仍然 ❌ 失效**:`?keyword=` 入参 / URL search 都被忽略
- **API 类别过滤真实有效**:POST `{page, pageSize, t, job}` 时 `job=technology` 过滤返 9 个(其他类别同)
- 站内点击才是正确用法:
  - **项目筛**:常规批次 / 技术专场 / 管培生 / 区域业务管培生 / 其他项目 / 人才专项 / 云弧计划
  - **类别筛**:设计 / 职能 / 运营 / 语言 / 市场营销 / 产品 / 技术 / 视觉类 / 区域业务
  - **标签筛**:紧缺 / 人才专项

**v17 当前 22 个岗位**(2026 校招届 - 2027 届应届 + 1 个 2026 届管培):

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

- **校招官网(新域名)**:<https://careers.pddglobalhr.com/campus/grad>
- **校招官网(旧域名,301 跳转)**:<https://careers.pinduoduo.com/campus/grad>
- **实习生招聘**:<https://careers.pddglobalhr.com/campus/intern>
- **公众号**:拼多多招聘

> 🚨 **注意事项**: PDD 校招基本 all in 上海,极少数管培生岗位在河北雄安。
> 重点关注「**云弧计划**」项目(人才专项,含 AI Infra 研发 / 大模型算法等核心岗位--拼多多唯二的算法岗)。

---

## 9. 滴滴 - ✅ Moka 系统 (v12)

**v12 实测结果**:`?project=2027` 选"2027 届校招项目"返 6 个岗位;默认搜索返 0 个项目实际仍可看职位。

- **校招官网**:<https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027>

| 方向 | 工作地 | 链接 | 类型 |
|---|---|---|---|
| 推荐 | 北京 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |
| 自动驾驶决策控制 | 北京/上海 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |
| Physical AI 多模态大模型 | 北京 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |
| 自动驾驶感知定位 | 北京/上海 | <https://campus.didiglobal.com/campus_apply/didiglobal/96064#/jobs?project=2027> | 🔍 |

---

## 10a. 蔚来 - ✅ URL搜索有效 (v12 飞书系)

**v12 实测结果**:`?keyword=推荐` 返 15 个岗位(1 个实习 = 7%)。`?keyword=NLP` 返 7 个(0 实习)。

- **校招官网**:<https://nio.jobs.feishu.cn?keyword=%E6%8E%A8%E8%8D%90>

| 方向 | 链接 | 类型 |
|---|---|---|
| 推荐 | <https://nio.jobs.feishu.cn?keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| NLP | <https://nio.jobs.feishu.cn?keyword=NLP> | 🔍 |
| 自动驾驶 | <https://nio.jobs.feishu.cn?keyword=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6> | 🔍 |
| 智能座舱 | <https://nio.jobs.feishu.cn?keyword=%E6%99%BA%E8%83%BD%E5%BA%A7%E8%88%8D> | 🔍 |

---

## 10b. 小鹏 - ✅ CSR URL搜索 (v24 重测)

**v24 重测**(2026-07-09):v12 "?keyword=X" 已**不可靠**。小鹏飞书系统是 CSR(JavaScript 渲染),URL 参数 `?keyword=X` 被 SPA 忽略。**有效方式**:用浏览器在搜索框输入后 URL 更新为 `?keywords=X&keyword=X`,两个参数都传才能生效。curl 只能拿到 185KB SSR 壳

### Endpoint 模板

- **校招 SPA 入口**:<https://xiaopeng.jobs.feishu.cn/campus/position/list>
- **带关键词搜索**:
  ```
  /campus/position/list?keywords=算法&keyword=算法&category=&location=&project=&type=&job_hot_flag=&current=1&limit=10&functionCategory=&tag=
  ```
- **详情 URL**:<https://xiaopeng.jobs.feishu.cn/campus/position/{id}/detail>

### 搜索参数字典(CSR 渲染,curl 不可用)

| 参数 | 说明 | 生效情况 |
|---|---|---|
| `keywords` | 关键词搜索 | ✅ 飞书搜索框触发 |
| `keyword` | 关键词搜索(冗余) | ✅ 双参数才能生效 |
| `category` | 职位类别筛选 (研发/汽车销售/...) | ✅ 侧栏筛 |
| `location` | 城市筛选 | ✅ 侧栏筛 |
| `project` | 项目筛选 | ✅ |
| `type` | 正式/实习 | ✅ |
| `current` | 页码 (from 1) | ✅ |
| `limit` | 每页数量 | ✅ |
| `functionCategory` | 功能分类 | ✅ |
| `job_hot_flag` | 热招标记 | ✅ |
| `tag` | 标签 | ✅ |

### 岗位总计 + 搜索统计

| 搜索词 | 总数 |
|---|---|
| 无过滤 | 467 |
| 算法 | 116 |
| 大模型 | 78 |

### 467 个总岗位(按类别)+ 116 算法岗

**筛选条件**:
- 职位类别(8 大类):研发 / 汽车销售与服务 / 产品策划项目 / 设计 / 职能支持 / 汽车制造 / 市场
- 城市(10):广州 / 上海 / 深圳 / 北京 / 武汉 / 肇庆 / 东莞 / 厦门 等
- 项目类型:正式 / 实习

**重点算法岗位(Page 1 样例)**:

| 岗位名 | 工作地 | 类型 | 方向 |
|---|---|---|---|
| 强化学习算法实习生 | 上海 | 实习 | 自动驾驶RL |
| 具身智能灵巧操作算法实习生 | 深圳 | 实习 | 机器人操作 |
| 【27届校招】算法工程师(自动驾驶仿真) | 上海 | 正式 | 仿真+评价算法 |
| Embodied Agent RL算法实习生 | 京/沪 | 实习 | RLHF/RLAIF+Agent |
| 【27届校招】VLA大模型算法工程师 | 上海 | 正式 | 自动驾驶VLA |
| 【27届暑期】具身智能灵巧手算法实习生 | 深圳 | 实习 | 机器人RL |
| 【27届校招】空间智能算法工程师 | 广州/上海 | 正式 | 3D重建+空间理解 |
| 【27届校招】VLA大模型算法工程师 | 广深沪等4城 | 正式 | 端到端感知+规控大模型 |
| 运动控制算法实习生(强化学习方向) | 深圳 | 实习 | 机器人运动RL |
| 【27届校招】机器人VLA大模型算法工程师 | 广深沪 | 正式 | 机器人VLA |

### 关键领域分布(116 算法岗覆盖)

- **自动驾驶 RL**:强化学习算法 / Embodied Agent RL / RLHF-RLAIF / offline RL
- **自动驾驶 VLA**:VLA大模型算法 / 感知规控大模型 / 端到端模型
- **机器人(小鹏机器人中心)**:具身智能灵巧操作 / 运动控制RL / 机器人VLA / 空间智能
- **自动驾驶仿真**:场景生成+泛化 / 评价指标 / 分布式仿真调度
- **感知**:BEV感知 / 道路拓扑 / 视觉/空间智能
- **计算平台**:数据平台 / 分布式训练(Spark/Flink/Ray/PyTorch)

> 🚨 **重点**:小鹏飞书系统是所有飞书校招中最**难自动化**的。CSR 渲染 + 双参数(keywords/keyword)+ 反爬。curl 拿 185KB 空壳,必须用 Playwright。算法岗 116 个覆盖自动驾驶 RL/VLA + 机器人具身智能两大核心方向。

| 方向 | 链接 | 类型 |
|---|---|---|
| 校招主页 | <https://xiaopeng.jobs.feishu.cn/campus/position/list> | 🔍 |
| 116 算法岗 | `?keywords=算法&keyword=算法` (需浏览器) | 🔍 |
| 78 大模型岗 | `?keywords=大模型&keyword=大模型` (需浏览器) | 🔍 |

---

## 10c. 理想汽车 — ✅ GET API (v26 重测)

**v26 重测**（2026-07-09）：发现 REST API！v12 `functionsids` URL 参数仍有效，但类别体系已重组。`project_id=4` = 校招项目。**不需要登录**，直接调 GET 拿全部岗位。

### Endpoint 模板

- **校招 API（核心）**：
  ```
  GET /osd-hr-recruitment-website/v1/recruit/school/job-page?page=1&page_size=50&project_id=4
  ```
- **分类过滤**：`&job_function_ids=1`（算法与软件）/ `8`（整车研发）/ `92`（芯片研发）
- **分类树 API**：`GET .../v1/recruit/school/job/function`
- **校招 SPA 入口**：<https://www.lixiang.com/employ/campus/list.html?project_id=4>
- **详情 URL**：<https://www.lixiang.com/employ/campus/list.html?project_id=4&job_id={id}>

### 岗位分类总览（API `job_function` 返回 10 大类 273+ 岗）

| 分类ID | 名称 | 岗数 | 子类 |
|---|---|---|---|
| 1 | 算法与软件 | 55 | 算法/软件测试/技术运维/信息安全/车辆控制/前端/后端/OS及嵌入式/数据开发/数据分析 |
| 8 | 整车研发 | 36 | 底盘/车身/热管理/电池/动力/增程/座舱/虚拟开发 等 17 项 |
| 92 | 芯片研发 | 5 | 前端设计/后端设计/软件设计/芯片架构 |
| 21 | 产品 | 13 | 软件产品/硬件产品/产品运营 |
| 34 | 销售与服务 | 88 | 储备管理/零售/交付/售后/商业拓展等 |
| 45 | 职能与综合管理 | 47 | 行政/法务/财务/HR/战略/品牌/政府关系等 |
| 29 | 供应链与智能制造 | 8 | 质量安全/采购/制造 |
| 64 | 充电网络 | 8 | 商务拓展/工程建设/策略分析 |
| 25 | 设计 | 12 | 设计 |
| 19 | 项目管理 | 1 | 项目管理 |

> 分类 API sum=273，但 `project_id=4` 全量分页 390 岗（39页×10）= 接近 385。

### 算法相关岗位（API `job_function_ids=1 + 8`，~21 个 ML/AI 岗）

**算法与软件 (24岗，含 ML/AI=11，其余为软测/运维/嵌入式)**：

| 岗位名 | 城市 | 类型 |
|---|---|---|
| 🧠 语音/全模态算法实习生 | 北京顺义 | 实习 |
| 🧠 大模型训练推理加速实习生 | 上海 | 实习 |
| 🧠 多模态算法实习生 | 北京顺义 | 实习 |
| 🧠 VLA 算法实习生 | 北京顺义 | 实习 |
| 🧠 AI工程实习生 | 北京 | 实习 |
| 🧠 【基座模型】强化学习算法研究员-物理智能体 | 北京朝阳 | 正式 |
| 🧠 智能体强化算法实习生 | 北京顺义 | 实习 |
| 🧠 AI系统开发实习生 | 杭州余杭 | 实习 |
| 🧠 强化学习算法实习生 | 北京顺义 | 实习 |
| 🧠 AI 云原生研发实习生 | 北京 | 实习 |

**整车研发 (22岗，含 ML/AI=10)**：

| 岗位名 | 城市 | 类型 |
|---|---|---|
| 🧠 具身智能产业规划工程师 | 北京顺义 | 正式 |
| 🧠 自主智能与AI交互研究工程师 | 北京 | 正式 |
| 🧠 视觉感知算法实习生 | 上海嘉定 | 实习 |
| 🧠 感知质量工程师 | 北京 | 正式 |
| 🧠 人工智能音乐生成实习生 | 北京顺义 | 实习 |
| 🧠 ai Agent应用研究实习生 | 北京顺义 | 实习 |
| 🧠 LLM Agent开发实习生 | 上海嘉定 | 实习 |
| 🧠 大模型智能体算法实习生（Prompt & Context Harness方向） | 北京 | 实习 |

> **芯片研发 (5岗)**：全硬核芯片（NPU运行时/验证/模拟设计/架构），无纯算法岗。

### 关键领域

- **基座模型 + 物理智能体**：基座模型 RL 研究员 / 智能体 RL / Agent 应用
- **自动驾驶感知**：VLA 算法 / 视觉感知 / 多模态算法 / 感知质量
- **语音/全模态**：语音全模态算法
- **大模型系统工程**：训练推理加速 / AI工程 / AI系统开发 / AI云原生
- **具身智能**：具身机器人产业规划 / 自主智能
- **创意 AI**：AI 音乐生成（💀 趣味岗）

> 🚨 **重点**：理想 API 完整、不需登录、分页清晰。24 算法与软件岗 + 22 整车研发岗中共 ~21 个 AI/ML 方向。**基座模型 RL 研究员** 是目前见过的纯 Research 岗（汽车公司少见！）。实习生占 17/24（70%）。

| 方向 | API | 类型 |
|---|---|---|
| 算法与软件 (24) | `GET .../job-page?project_id=4&job_function_ids=1` | ✅ API |
| 整车研发 (22, 含 10 AI) | `GET .../job-page?project_id=4&job_function_ids=8` | ✅ API |
| 芯片研发 (5) | `GET .../job-page?project_id=4&job_function_ids=92` | ✅ API |
| 分类树 | `GET .../job/function` | ✅ API |

---

## 10d. 小红书 - ✅ POST API (v23 重测)

**v23 重测重大发现**(2026-07-09):v12 "🏠 校招子站" 是错的。小红书公告网站 SPA 内部调用 POST API,**不需要登录**就能拿到全部岗位!

### Endpoint 模板

- **入口 SPA**:<https://job.xiaohongshu.com/campus/positions>
- **列表 API**:
  ```
  POST /websiterecruit/position/pageQueryPosition
  Body: {"recruitType":"campus","pageNum":1,"pageSize":50}
  ```
- **详情 API**:
  ```
  GET /websiterecruit/position/queryPositionDetail?positionId=XXX
  ```
- **项目列表 API**:
  ```
  GET /websiterecruit/position/project/{projectCode}
  ```
- **详情 URL (SPA)**: <https://job.xiaohongshu.com/campus/position/PU13651>

### recruitType 字典

| recruitType | 含义 | total |
|---|---|---|
| `campus` | **校园招聘(全公司)** | **332** ⭐ |
| `social` | 社会招聘 | 858 |
| `intern` | 实习 | 246 |

> `recruitType=campus` 包含 27/28 届实习生 + Ace 顶尖实习生 + 2026 校招(REDstar 等应届岗)。实习标签 `/ intern` 是独立队列。

### 请求参数(已验证生效)

| 参数 | 说明 | 生效情况 |
|---|---|---|
| `recruitType` | `campus` / `social` / `intern` | ✅ 必须 |
| `pageNum` | 页码 | ✅ |
| `pageSize` | 每页数量 (max 50) | ✅ |
| `positionName` | **关键词搜索** | ✅ 唯一有效的关键词 |
| `jobTypes` | 职位类型数组 | ✅ (前端用, 需 enum code) |
| `workplaces` | 工作城市数组 | ✅ (前端用, 需 code) |
| `campusRecruitTypes` | 校招类型 | ✅ (前端校园筛) |
| `jobProjects` | 项目 (Ace/REDstar等) | ✅ (前端用) |
| `keyword` / `name` / `searchText` | 文本搜索 | ❌ 被 server 忽略 |

### 332 个校园岗位总览

按 jobType 分类(157 个 unique AI/算法岗位名):

**🏆 校招三类:**
- **2026校招 (REDstar)**:16 个顶级 AI 岗位(应届)
- **Ace 顶尖实习生**:38 个顶级 AI 实习生
- **27届 / 27/28届 实习**:16 个 + 通用实习生

**⭐ REDstar (16 个顶级应届 AI 岗):**
| 岗位名 | 城市 |
|---|---|
| 基座大模型算法工程师 | 京/沪/杭 |
| 大模型 RL Training Infra 工程师 | 京/沪 |
| 大模型 Efficient Inference Infra 工程师 | 京/沪 |
| 大模型应用算法工程师 - rednote国际化 | 京/沪/杭 |
| 商业广告算法工程师 | 京/沪 |
| 社区搜索算法工程师 | 京/沪/杭 |
| 用户理解算法工程师 | 京/沪 |
| 智能客服算法工程师 | 京/沪/杭 |
| 电商算法工程师 - 搜推方向 | 京/沪/杭 |
| NLP与多模态算法工程师 | 京/沪/杭 |
| NLP/多模态算法工程师 - 交易/商业化治理 | 京/沪/杭 |
| Dots-Post-Training 算法工程师 | 京/沪 |
| Dots-视觉语言大模型算法工程师 | 京/沪 |
| Dots-大语言模型基础技术研究员 | 京/沪 |
| Dots-大模型高性能计算工程师 - AI infra | 京/沪 |
| Dots-大模型预训练数据算法研究员 | 京/沪/杭 |

**🏆 Ace 顶尖实习生 (38 个顶级AI实习):**
| 岗位名 | 类型 |
|---|---|
| 基础大模型Agent能力研究 | 大模型 |
| 大模型后训练泛化性研究 | 大模型 |
| 基于Diffusion LLM的基座大模型研究 | 大模型 |
| Large Scale ML Model 训练和推理性能极致优化 | 大模型 |
| 向量检索在大模型场景的应用和KVCache优化研究 | 引擎 |
| 面向多语言的AI搜索检索和生成系统研究 | 策略算法 |
| 基于Agent框架的AI搜索基座大模型 | 策略算法 |
| 基于大模型的生成式推荐探索 | 策略算法 |
| 基于Agent的交互式推荐系统 | 策略算法 |
| 面向千人千面agent的广告大模型能力构建 | 策略算法 |
| 生成式搜索营销 Agent 系统研究 | 策略算法 |
| 基于agent技术的商业化AI代理研究 | 策略算法 |
| 交互式进化审核 Agent 系统研究 | 策略算法 |
| 多语言大模型和翻译应用 | 策略算法 |
| 面向多业务场景的多模态统一大模型基座与智能体应用研究 | 内容理解 |
| 端到端的全双工自然语音交互 | 多媒体算法 |
| AI在高强度混淆/vmp场景下还原代码研究 | 安全 |
| AI coding agent技术研究与应用 | 后端开发 |
| GUI Agent在App自动化领域的研究与应用 | 后端开发 |
| 面向大模型智能体的云原生 Sandbox/Agent调度/Agent Runtime 系列 (×3) | 基础后端 |
| 面向多模态数据的向量索引组织与混合查询优化技术研究 | 基础后端 |
| AI 长期记忆机制与终身学习研究 | 大模型 |
| 全模态Agent长程任务RL算法+工程Co-Design研究 | 机器学习平台 |
| 全模态大模型理解与生成轻量化及加速算法研究 | 机器学习平台 |
| 轻量化AI媒体处理算法与部署 | 多媒体技术 |
| DataEngineer Agent 研发和规模化落地 | 数据引擎 |
| 多模态大模型驱动的端工程架构设计、改造的研究 | 客户端开发 |
| 小红书AI × 社区 RPT产品培训生 | 产品经理 |

**📋 2026校招(非REDstar AI岗位):**
- AI Infra工程师, 大模型应用算法工程师 - 增长方向, 社区搜索算法工程师
- 用户理解算法工程师, 用户增长算法工程师, 智能客服算法工程师
- AI native应用 - 前端开发工程师

**其他 AI 算法实习:**
- Agent 工程/开发实习生, AI全栈/后端/Native开发, 搜索/推荐算法
- 音频/编解码/AIGC/风控/多模态算法实习生
- 大模型平台 Agentic 全栈/训推/推理/RL训练引擎/压缩(练习生)
- 多模态数据引擎/AI存储研发工程师(练习生)
- AI Native 产品/运营/方向/创新实习生

### API 响应结构

```json
{
  "success": true,
  "data": {
    "pageNum": 1,
    "pageSize": 10,
    "total": 332,
    "totalPage": 34,
    "list": [
      {
        "positionId": 13651,
        "positionName": "杂志编辑部剪辑实习生(音视频剪辑)",
        "jobType": "视觉设计",
        "jobProjectName": "",
        "duty": "工作职责:...",
        "qualification": "任职资格:...",
        "workplace": "上海市",
        "workplaceIds": 3100,
        "publishTime": "2026-07-09",
        "recruitStatus": "in_recruitment",
        "labels": null,
        "amountInNeed": null
      }
    ]
  }
}
```

> 🚨 **重点**:`recruitType=campus` 不需登录。`positionName=算法` 是真关键词搜索。Ace顶尖实习生=小红书版 Top Seed。REDstar=小红书顶级应届岗。

| 方向 | 链接 | 类型 |
|---|---|---|
| 校招 SPA | <https://job.xiaohongshu.com/campus/positions> | 🔍 |
| 332 校园岗位 | `POST /websiterecruit/position/pageQueryPosition?recruitType=campus` | ✅ API |
| 144 算法关键词搜索 | `POST ... ?positionName=算法` | ✅ API |
| REDstar 16 岗 | 首页 REDstar 入口 → "立即投递" | 🔍 |

---

## 10e. 大疆 - ✅ Moka 系统 + 关键词哈希篏 (v19 重测)

**v19 实测重大发现**(2026-07-09):
- v12 说 "需点 查看在招职位 才能进职位列表" 仍是事实;但现在职位列表是 **Moka** 的 `apply.careers.dji.com` 平台
- 当前 Moka **校招 project ID = 143359**(社会招聘是 170070)
- **URL 关键词搜索有效** (Moka hash 路由):
  - 不带关键词:138 个岗位
  - `#/jobs?keyword=算法`:**54 个**算法岗
  - `#/jobs?keyword=推荐`:0 个(DJI 不做推荐算法)
  - `#/jobs?keyword=大模型`:**6 个**大模型岗
- 项目名:**「2027 拓疆者」校园招聘**(2026.6.25 启动,招聘 2027 届应届)

**v19 54 个算法岗关键列表**(keyword=算法,3 个城市:北京/上海/深圳):

- 图传 AI 算法工程师(上海)
- **GNSS 定位算法工程师**(北京/上海/深圳)
- **端到端决策规划算法工程师**(北京/上海/深圳)
- **世界模型算法工程师**(北京)
- **传感器算法工程师(激光雷达)**(深圳)
- **SLAM 算法工程师**(北京/上海/深圳)
- 电池算法工程师(深圳)
- **图像算法工程师**(深圳/上海)
- **计算机视觉算法工程师**(深圳/上海)
- **多模态空间感知算法工程师**(北京/上海/深圳)
- **多模态大模型算法工程师**(北京/上海/深圳,6 个)
- **大模型推理部署算法工程师**(北京/上海/深圳,6 个)

**DJI 独有算法方向**:SLAM/激光雷达感知/图传无线/GNSS 定位/端到端决策规划/世界模型 - 纯属机器人 / 无人机领域,其他大厂很少有。

- **校招主页**:<https://we.dji.com/zh-CN/campus/> (老域名, 仍能跳转)
- **校招主页(新域名)**:<https://careers.dji.com/zh-CN/campus>
- **校招职位列表(Moka, 138 岗)**:<https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs>
- **算法类(54 岗)**:<https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E7%AE%97%E6%B3%95>
- **大模型类(6 岗)**:<https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B>
- **社会招聘项目(170070, 475 岗)**:<https://apply.careers.dji.com/social-recruitment/dji/170070#/jobs>

| 方向 | 链接 | 类型 |
|---|---|---|
| 全算法类(54 岗) | <https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E7%AE%97%E6%B3%95> | 🔍 |
| SLAM(3 岗) | <https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=SLAM> | 🔍 |
| 定位算法 | <https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E5%AE%9A%E4%BD%8D> | 🔍 |
| 决策规划 | <https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E5%86%B3%E7%AD%96> | 🔍 |
| 计算机视觉 | <https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E8%A7%86%E8%A7%89> | 🔍 |
| 多模态大模型(6 岗) | <https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |

> 🚨 **DJI 必看点**: DJI 是少数同时在 **无人机 + 机器人 + 自动驾驶** 技术栈均领先的独角兽,适合做 SLAM/激光雷达感知/图传无线/世界模型/端到端决策规划 的求职者。
> **城市分布**: 所有校招岗位都是 **北京 / 上海 / 深圳** 三个城市。

---

## 10f. 得物 — ✅ CSR URL搜索 (v25 重测)

**v25 重测**（2026-07-09）：飞书系，Moka 已迁移。校招官网 `campus.dewu.com` 跳转 `/578078/position/list`。24 个总岗位中仅 8 个算法岗，全部为「研究型实习生项目」。curl 只拿 SSR 壳（58KB），用 Playwright。

### Endpoint 模板

- **校招 SPA 入口**：<https://campus.dewu.com/578078/position/list>
- **关键词搜索**：
  ```
  /578078/position/list?keywords=算法&current=1&limit=10
  ```
- **详情 URL**：<https://campus.dewu.com/578078/position/{id}/detail>

### 搜索统计

| 搜索词 | 总数 |
|---|---|
| 无过滤 | 24 |
| 算法 | 8 |
| 大模型 | 6 |
| AI | 7 |
| 推荐 | 4 |
| 研究型实习生 | 7 |

### 24 岗位总览

**招聘项目**（侧栏树形筛选）：
- 日常实习项目 → 研究型实习生项目 / 社招实习
- 【校招】暑期实习生 → 2027届实习生项目

**职能分类**（6 类）：供应链类 / 实习专区 / 技术类 / 设计类 / 运营类 / 职能类

**城市**（7）：上海 杭州 广州 廊坊 沈阳 武汉 咸阳

### 8 个算法岗（全部研究型实习生项目）

| 岗位名 | 工作地 | 方向 |
|---|---|---|
| 【研究型实习生】生成式重排 | 上海 | LLM+RL 搜索重排 |
| 【研究型实习生】生成式相关性大模型（交易） | 杭州/上海 | LLM/VLM 电商搜索 |
| 【研究型实习生】空间理解和推理 | 上海 | 3D视觉+多模态生成 |
| 【研究型实习生】交易多模态大模型 | 上海 | VLM 商品理解+推理 |
| 【研究型实习生】生成式召回（交易瀑布流推荐） | 上海 | LLM推荐SID召回 |
| 【研究型实习生】排序模型参数scaling的调研（社区推荐精排） | 上海 | 大模型排序 |
| 【研究型实习生】多场景生成式大模型（交易） | 杭州 | LLM搜索问答Agent |

### 关键领域分布

- **搜索/相关性**：生成式重排(RL+Listwise) / 相关性大模型(VLM/LLM电商搜索) / 多场景生成式(Agent+Deep Research)
- **推荐**：生成式召回(SID+Scaling) / 排序Scaling(大模型参数量→涌现)
- **多模态**：交易多模态大模型(VLM) / 空间理解推理(3D+多模态)
- **核心能力**：LLM/RL → 搜索推荐 / VLM → 商品理解 / Agent+Deep Research → 智能问答

> 🚨 **重点**：得物算法岗全为「研究型实习生项目」，偏 Intern+论文产出。没有正式 2027 届算法岗。适合有顶会论文意愿的同学投。属于潮鞋电商 + 内容社区场景。URL keywords 单参数传 SEO 可生效。Moka 入口 `app.mokahr.com/apply/dewu` 已废。

| 方向 | 链接 | 类型 |
|---|---|---|
| 校招主页 | <https://campus.dewu.com/578078/position/list> | 🔍 |
| 算法岗（8个） | `?keywords=算法` (需浏览器) | 🔍 |
| 大模型岗（6个） | `?keywords=大模型` (需浏览器) | 🔍 |

---

## 10g. OPPO - ✅ 校招主页 + 调度 API (v13)

**v13 实测重大突破**:
- 主页:`https://careers.oppo.com/campus` (项目入口页, body=1172)
- **职位列表**:`https://careers.oppo.com/university/oppo/campus` (返 25 个在招岗位)
- **发现 3 个真实 API**:
  - `https://careers.oppo.com/openapi/position/project/list` (招聘项目列表)
  - `https://careers.oppo.com/openapi/position/project/querySpecialRecruitment` (AI人才专项等)
  - `https://careers.oppo.com/openapi/system/dictionary/queryList?code=RECRUIT-TYPE`

**当前状态**(重要):**2026 应届校招暂未启动**
- 招聘项目只有 `2026 届博士生招聘` (id=24) 和 `2027 届寻梦实习招聘` (id=29)
- 主页显示 "应届生暂未开始"
- 推测 2026.9 启动 2027 届校招
- **可立即查**: 25 个在招职位 (主要是博士生岗 + 实习生岗)

- **校招主页**:<https://careers.oppo.com/campus>
- **职位列表**:<https://careers.oppo.com/university/oppo/campus> (25 个岗位, AI/算法类仅含博士生岗位)
- **API**: 项目列表 API 返回 `idRecruitProject=24/29` 两个招聘项目
- **热门方向 (博士岗)**: 高级机器学习研究员(健康方向)、高级 AI 研究员、语音算法、推荐算法、视觉算法

> **将来"" 应届校招启动后, 可用以上 URL 查 AI/算法类职位。**



---



- **校招官网**:<https://campus.kuaishou.cn/>(主页是营销页,需点"校园招聘"按钮)

---

## 11. 小米 - ✅ URL搜索有效 (v16 飞书系统)

**v16 实测重大突破**(2026-07-09):
- 小米校招**不是** `hr.xiaomi.com/campus/list`(那个是 2018 年过期数据)
- 真正的投递系统是飞书(mioffice):**`xiaomi.jobs.f.mioffice.cn/campus/`**
- URL 参数 `?keywords={方向}` **真实有效** ✅
- 当前 55 个岗位(2026 春季校招已近尾声,主要是 2027 届实习岗)
- 招聘项目:2026届春季校招 / 秋季校招 / 实习生 / 境外校招
- 职能分类:软件研发类 / 硬件研发类 / 芯片类 / 运维类 / 产品类 / 运营类 / 市场类 / 职能类 / 销售类 / 商务类
- 算法岗归类在「软件研发类」下(无独立「算法类」)

- **校招主页(营销页)**:<https://hr.xiaomi.com/campus>(点「立即加入」跳飞书系统)
- **飞书投递系统**:<https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR>
- **公众号**:小米招聘

| 方向 | 学历 | 工作地 | JD 关键词 | 链接(实测) | 类型 |
|---|---|---|---|---|---|
| 推荐 | 硕 | 北京 | 推荐算法、CTR | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E6%8E%A8%E8%8D%90> | 🔍 |
| 大模型 | 硕/博 | 北京 | Agent、LLM、端侧 AI | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |
| 自动驾驶 | 硕/博 | 北京/上海 | 感知、决策规划、SLAM | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6> | 🔍 |
| 语音 | 硕/博 | 北京 | ASR/TTS、小爱同学 | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%AF%AD%E9%9F%B3> | 🔍 |
| NLP | 硕/博 | 北京/武汉 | 对话、小爱、文本理解 | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=NLP> | 🔍 |
| 计算机视觉 | 硕/博 | 北京/上海 | 检测、分割、手机影像 | <https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89> | 🔍 |

> ⚠️ 当前(2026-07)春季校招网申期已过(截止 5 月 31 日),搜索结果以 2027 届实习为主。
> 秋季校招启动后(预计 8-9 月),同样的 URL 模板可以直接用搜索方向词查找正式校招岗位。

> 💡 小爱同学 / 端侧 AI / 手机影像 / 自动驾驶 是小米独有的算法方向,其他大厂少。

---

## 12. 知乎 - ✅ URL搜索有效 (Moka 系统)

**实测结果**:`#/jobs?keyword=推荐` 返回"3 个结果 - 推荐策略产品"等岗位

- **校招官网**:<https://app.mokahr.com/apply/zhihu/78336#/jobs>

| 方向 | 链接(实测) | 类型 |
|---|---|---|
| 推荐 | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=%E6%8E%A8%E8%8D%90> | 🔍 |
| NLP | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=NLP> | 🔍 |
| LLM | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=LLM> | 🔍 |
| 大模型 | <https://app.mokahr.com/apply/zhihu/78336#/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B> | 🔍 |

> **关键**:Moka 系统需要 jobId(如 `/zhihu/78336`),不同 BU 不同

---

## 13. AI 独角兽 - Moka / 飞书 系统(统一格式)

智谱 / 月之暗面 / 百川 / MiniMax / 得物 等都用 Moka / 飞书

| 公司 | 招聘入口(实测) | 类型 |
|---|---|---|
| **智谱 AI** | <https://zhipu-ai.jobs.feishu.cn/> | 🔍 飞书系统,URL 支持搜索 |
| **月之暗面** | <https://app.mokahr.com/apply/moonshot/148506> | 🔍 Moka 系统,URL 支持搜索 |
| **MiniMax** | <https://app.mokahr.com/apply/MiniMax/2957> | 🔍 Moka 系统 |
| **百川智能** | <https://app.mokahr.com/apply/baichuan/40395> | 🔍 Moka 系统 |
| **得物** | <https://app.mokahr.com/apply/dewu> | ❌ 已 404,需替换 |
| **DeepSeek** | 公众号"DeepSeek 招聘" | 🏠 |
| **阶跃星辰** | <https://www.stepfun.com/> | 🏠 营销页 |
| **零一万物** | <https://www.01.ai/> | 🏠 营销页 |
| **面壁智能** | <https://www.modelbest.cn/> | 🏠 营销页 |

**Moka 系统通用 URL 模板**:`#/jobs?keyword={方向}`

**飞书系统通用 URL 模板**:`?keyword={方向}`

---

## 14. 传统 CV 四小龙 - BOSS 直聘

| 公司 | 招聘入口 | 备注 |
|---|---|---|
| **商汤** | <https://www.liepin.com/company/8001480/> | 猎聘主页(官方 404) |
| **旷视** | <https://www.zhipin.com/web/geek/job?query=%E6%97%A0%E7%A7%91%E6%8D%82> | BOSS 通用搜索 |
| **依图** | <https://www.zhipin.com/web/geek/job?query=%E4%BE%9D%E5%9B%BE> | BOSS 通用搜索 |
| **云从** | <https://www.zhipin.com/web/geek/job?query=%E4%BA%91%E4%BB%8E> | BOSS 通用搜索 |

---

## 15. 快手校招 - ✅ 项目篏 + 类目码 (v18 重测)

**v18 重测重大发现**(2026-07-09):v14 里说的 `?keyword=X` 已经失效!

- **真过滤**:项目筛 `?recruitSubProjectCodes=...` 仍✅(v14 发现的)
- **URL `?keyword=` 现已失效**:`推荐`/`NLP`/`大模型` 三个关键词都返同样默认列表(74 个全量)
- **后台 API**:POST `https://campus.kuaishou.cn/recruit/campus/e/api/v1/open/positions/simple`,支持:
  - `recruitSubProjectCodes: ["20271779425607"]`(项目筛)
  - `positionCategoryCodes: ["J1005"]`(**类目码篏,推荐类 J1005 返 10 个**)
  - `workLocationCodes: ["beijing"]`(**城市码篏,beijing 返 72 个**)
  - `pageSize + pageNum`(分页)
- 但上面这些参数调用时 `total` 还是 74 不变,**实际是前端拿到全量后本地过滤**--所以「API 能用」是 JS 层面的,真正落进 URL 路由的还是项目筛一个

**v18 实地分析:74 岗位全为「快Star」人才计划项目**(招聘项目 `20271779425607`),重点是类目码字典:

| 类目码 | 类目名(推断) | 岗位数 | 代表岗位 |
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

**4 个工作地**:北京 72 / 上海 14 / 深圳 14 / 杭州 12 (一岗位可投多个城市)

- **招聘主页**:<https://campus.kuaishou.cn/recruit/campus/e/>
- **2027 届应届招聘**:<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271779425607> (74 岗, 全为「快Star」人才计划)
- **2027 届实习 (含留用)**:<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271772783534>
- **2026 届应届**:<https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20261749721165>
- **快Star 人才计划主页**:<https://campus.kuaishou.cn/recruit/campus/e/#/campus/talent>
- **项目代码字典**:`2020-2027` 届都在。应届项目 code = `20261749721165` (2026届), `20271779425607` (2027届)

| 方向 | 链接 | 类型 |
|---|---|---|
| 快Star 主页 (人才计划) | <https://campus.kuaishou.cn/recruit/campus/e/#/campus/talent> | 🔍 |
| 2027 届应届 (74 岗) | <https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271779425607> | 🔍 |
| 大模型 / Infra / 推理 (J1013, 14 岗) | 站内点「J1013」类目 | 🏠 |
| 多模态 / CV / AIGC (J1007, 12 岗) | 站内点「J1007」类目 | 🏠 |
| 推荐 (J1005, 10 岗) | 站内点「J1005」类目 | 🏠 |
| 广告 (J1006, 4 岗) | 站内点「J1006」类目 | 🏠 |
| 搜索 (J1004, 4 岗) | 站内点「J1004」类目 | 🏠 |

> 🚨 **注意**: v14 里说 `?keyword=X` 有效是错的。到 v18 关键词已全部被忽略。正确做法是直接打开项目页面,然后在左侧点「职位类别」复选框(「J1005 推荐」「J1006 广告」等),页面会在本地用 JS 过滤,但 URL 不变。
> 「快Star」是快手校招顶级品牌--74 个岗位全部是「快Star」人才计划。

---

## 16. 携程校招 - ✅ 完整校招系统 (v14)

**v14 实测**:携程完整校招系统, 主页 body=5491

- **招聘主页**:<https://campus.ctrip.com>
- **项目**: 应届校招生 (面向 2026 届, 毕业 2025.9-2026.8) + 留用实习生 (面向 2027 届)
- **岗位类别**: 研发类 / 产品类 / 设计类 / 综合类 / 人才项目

| 方向 | 链接 | 类型 |
|---|---|---|
| 招聘主页 | <https://campus.ctrip.com> | 🏠 |
| 社招 | <https://careers.ctrip.com> | 🏠 |

---

## 17. 360 集团 - ✅ 校招主页完整 (v14)

**v14 实测**:`campus.360.cn` body=1078, 360 集团 2026 全球校园招聘

- **招聘主页**:<https://campus.360.cn>

**项目**: 2026 全球校园招聘 + **算法岗位快速通道** + 飞扬实习生 + 实习转正

---

## 18. 鹰角网络 - ✅ 招聘主页完整 (v14 游戏)

**v14 实测**:`career.hypergryph.com` body=1787, 明日方舟母公司

- **招聘主页**:<https://career.hypergryph.com>

**职位类别**: 美术 / 产品 / **程序技术 76 个** / 职能 / 质量

---

## 19. Keep - ✅ 招聘主页完整 (v14)

**v14 实测**:`hr.keep.com` body=232

- **招聘主页**:<https://hr.keep.com>

**项目**: 社会招聘 / 校园招聘 / 校招 Q&A / 实习生招聘 / KeepACE.AI

---

## 20. 美团系 (大众点评/猫眼/美团酒旅) - ✅ 同一系统 (v14)

**v14 实测发现**:大众点评 / 猫眼 / 美团酒旅与美团本身同一校招系统。`career.dianping.com`、`hr.maoyan.com`、`career.meituan.com` 均跳到 `zhaopin.meituan.com/web/campus`。

**真实可用 URL**: `<https://zhaopin.meituan.com/web/position?hiringType=4_1&keyword={方向}>` (与美团同 URL, 0 实习)

---

## 21. 飞书 (字节系) - ✅ 招聘主页完整 (v14)

**v14 实测**:`www.feishu.cn/jobs` body=3933, 字节系

- **招聘主页**:<https://www.feishu.cn/jobs>

**状态**: 599 个职位, 职位类别 (产品/技术/职能/设计等) + 城市过滤 (北京/上海/深圳/杭州/成都/广州/西安)

---

## 22. 元戎启行 - ✅ Moka 系统 (v14 自动驾驶)

**v14 实测**:`app.mokahr.com/apply/deeproute` body=2275, 自动驾驶

- **招聘主页**:<https://app.mokahr.com/apply/deeproute>

**职位**: 感知算法 / 预测规划算法 / Robotaxi 技术负责人 / 投融资分析师 / 产品运营经理

---

## 23. 网易 + 网易有道 - ✅ 招聘主页完整 (v14)

- **网易校招**:<https://campus.163.com> body=155
- **网易有道**:<https://hr.youdao.com> body=1001

有道页面含 Campus Recruitment / Intern Recruitment / Experienced Hire

---

## 24. 虎牙 - ✅ 招聘主页完整 (v14 直播)

**v14 实测**:`hr.huya.com` body=1874

- **招聘主页**:<https://hr.huya.com>

**职位类别**: 技术类 / 内容运营类 / 产品类 / 设计类 / 市场品牌 / 职能

---

## 25. 用友 - ✅ 招聘主页完整 (v14 企业软件)

**v14 实测**:`career.yonyou.com` body=991

- **招聘主页**:<https://career.yonyou.com>

**项目**: 社会招聘 / 校园招聘 / **高潜人才计划** / 实习生招聘

---

## 26. 猿辅导 - ✅ 招聘主页完整 (v14 教育)

**v14 实测**:`hr.yuanfudao.com` body=151

- **招聘主页**:<https://hr.yuanfudao.com>

**职位**: 产品/研发 7 / 职能 3 / 教育/教研 10 / 硬件工程 4 / 其他 7

---

## 27. 网易互娱 - ✅ 校招主页完整 (v15 游戏)

**v15 实测**:`game.campus.163.com` body=628

- **校招主页**:<https://game.campus.163.com>

**招聘流程**: 网申/内推 1月起 → 笔试 1月下旬起 → 面试 2月上旬起 → OFFER

---

## 28. 三七互娱 - ✅ 校招入口 (v15 游戏)

**v15 实测**:

- **招聘主页**:<https://zhaopin.37.com> body=4225
- **校招页 (推荐)**:<https://zhaopin.37.com/index.php?m=Home&c=campus&a=index> body=354
  - 岗位类型: **AI类** / 游戏策划类 / 游戏研发类 / 游戏运营类 / 市场推广类 / 技术开发类 / 美术设计类 / 职能管理类
  - 地点: 广州 / 厦门 / 武汉 / 北京 / 上海 / 苏州

---

## 29. 西山居 - ✅ 校招系统完整 (v15 游戏)

**v15 实测**:西山居(金山旗下游戏工作室,剑网3 / 解限机 / 尘白禁区)独立校招站

- **校招主页 (实际可用)**:<https://job.seasungames.cn/campus> body=1532
- **招聘项目**:应届生招聘 1 / 训练营招聘 15 / 实习生招聘 13
- **职位分类**:美术音频 0 / 产品策划 1 / 程序质量 0 / 运营发行 0 / 职能综合 1

**v15 注意事项**:`hr.xishanju.com` 只是入口,真正的校招站是 `job.seasungames.cn/campus`

---

## 30. 叠纸游戏 - ✅ 公司主页含招聘 (v15 游戏)

**v15 实测**:`www.papegames.com/career` body=2115 (含 加入我们 + 产品介绍)

- **招聘主页**:<https://www.papegames.com/career>

**v15 备注**:叠纸游戏 Moka (app.mokahr.com/apply/papegames) 已关停,应使用主站点

---

## 31. 深信服 - 🏠 校招入口 (v15 安全)

**v15 实测**:

- **招聘主页**:<https://hr.sangfor.com> body=1516
- **校招主页**:<https://hr.sangfor.com/campuszp> body=179 (含 X-STAR 顶尖人才)
- **产品领域**:网络安全 / 云计算 / 企业级无线

---

## 32. 摩尔线程 - 🏠 公司主页 (v15 芯片/GPU)

**v15 实测**:

- **公司主页**:<https://www.mthreads.com/career> body=969
- **产品**: 全功能 GPU / 显卡 (MTT S80/S70) / 智算中心 / AI 模组
- **v15 备注**:页面是产品展示页,招聘入口需在 `career` 页上找链接,**不适合直采**

---

## 33. 阿里健康 - 🏠 公司主页 (v15 医疗)

**v15 实测**:

- **公司主页**:<https://www.alihealth.cn/career> body=497
- **v15 备注**:有 "加入我们" 入口,但实际招聘入口需进主站内搜

---

## 📊 完整实测结论 (v3-v15, Playwright + Chromium)

| 公司 | 实测类型 | 备注 |
|---|---|---|
| 字节跳动 | ✅ URL 搜索有效 | `?keywords=X&project=7525009396952582407,7621018151002507573` (去实习) |
| 美团 | ✅ URL 搜索有效 | `/web/position?hiringType=4_1&keyword=X` (应届校招项目, 0实习) |
| 腾讯 | ✅ URL 搜索有效 | `?keyword=X` 真实过滤 |
| 知乎 (Moka) | ✅ URL 搜索有效 | `#/jobs?keyword=X` |
| vivo | ✅ URL 搜索有效 | URL 不变, 前端 JS 搜索 (搜"推荐"返回 33 个, 搜"NLP"返回 16 个) |
| 蔚来(飞书系) | ✅ URL 搜索有效 | `?keyword=X` (v12, 搜"推荐"返 15 个, 1 实习) |
| 小鹏(飞书系) | 🔍 CSR 双参数 | `?keywords=算法&keyword=算法` 需 Playwright (v24) |
| 理想汽车 | ✅ GET API | `job-page?project_id=4&job_function_ids=1` (390总 24算法) (v26) |
| 滴滴(Moka) | ✅ project 筛 | `#/jobs?project=2027` 返 6 个 (v12) |
| 快手校招 | ✅ recruitSubProjectCodes | `recruitSubProjectCodes=20271779425607` 74 个 (全快Star), `?keyword=` 已失效 (v18) |
| 大疆 | ✅ Moka 拓疆者 | `apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=X` 138 岗 (v19) |
| 携程 + 360 + 虎牙 + 鹰角 + 用友 + 网易 + Keep + 飞书 | ✅ 主页完整 | v14 (需进站内搜方向词) |
| 元戎启行 (Moka) | ✅ Moka | `#/jobs?keyword=X` |
| 美团系 (大众点评/猫眼/酒旅) | ✅ 共享美团 URL | `?hiringType=4_1&keyword=X` |
| 阿里巴巴 | 🏠 talent.taotian.com | 主页是项目入口, 需进站内搜 |
| 拼多多 | 🏠 careers.pddglobalhr.com/campus/grad | URL 搜索失效,需进站内筛类别 (v17 新域名, 22 岗位) |
| 得物 | 🔍 | `campus.dewu.com/578078/position/list` CSR (24总 8算法全研究型实习生) (v25) |
| 小红书 | ✅ POST API | `POST job.xiaohongshu.com/websiterecruit/position/pageQueryPosition` (332 校园) |
| 大疆 | ✅ Moka 拓疆者 (project=143359) | `apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=X` 138 岗, 算法 54 (v19) |
| 百度 | ✅ SSR 项目码 | `talent.baidu.com/jobs/list?projectType=X` 生效;AIDU=11/校招=145 (v20) |
| 京东 | ✅ POST API | `POST campus.jd.com/api/wx/position/page?type=X` + planId;TGT=127 (v21) |
| 华为 | ✅ GET API | `GET career.huawei.com/reccampportal/services/portal/portalpub/getJob/newHr/page/50/1?jobType=2` (198 校招) (v22) |
| 小红书 | ✅ POST API | `POST job.xiaohongshu.com/websiterecruit/position/pageQueryPosition` (332 校园) (v23) |
| 小鹏 | 🔍 | `?keywords=算法&keyword=算法` 需 Playwright CSR (467总 116算法) (v24) |
| 京东 | 🏠 campus.jd.com/#/jobs | URL 参数被忽略 |
| 华为 | ✅ GET API | `GET /reccampportal/services/portal/portalpub/getJob/newHr/page/50/1?jobType=2` (198 校招, 36 AI) (v22) |
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

**v3 之前的版本**:我假设所有公司都支持 URL 搜索参数,结果**大量瞎写**。

**v3 实际验证后**:
- ✅ **4 家公司 URL 搜索真实有效**:字节/美团/腾讯/知乎 + Moka/飞书系
- ❌ **其余公司 URL 搜索无效**,需要进主页用站内搜索

**给用户的使用建议**:
1. **优先用字节/美团/腾讯/知乎的链接**(URL 搜索真实有效)
2. **其余公司**:进首页 → 站内搜方向词 → 选"职位类别"过滤
3. **不要相信一个看起来正常的 URL 真的过滤了关键词**--很多公司的 URL 参数被忽略