# job-pulse — 2026 校招算法岗情报站（实测版 v20）

> **v20：百度校招重测 → SSR 项目码筛生效；发现 AIDU 项目 (11 个顶级 AI 岗，类似字节 Top Seed)**
> **v18：快手校招重测 → v14 `?keyword=X` 已失效；发现 13 个类目码 (J1005 推荐/J1006 广告/...) 真过滤**
> **v17：拼多多已迁移到 careers.pddglobalhr.com，22 个校招岗位真实列表 (含 AI Infra/大模型算法核心岗)**
> **v16：小米校招实测 → 飞书 mioffice 系统，URL keywords 搜索真实有效**
> **v13：发现 OPPO 完整校招系统 + 3 个调度 API**
> **实测日期**：2026-07-07
> **方法**：用 Playwright 启动 Chromium，对每家公司执行"打开主页 + 搜索方向词 + 验证 URL 是否生效 + body 是否真的过滤 + 验证是否含实习岗"

## 🎯 v8 实测核心结论

**18 家公司实测后**：

| 类型 | 数量 | 公司 |
|---|---|---|
| ✅ **URL 搜索真实有效** | 6 | 字节 / 美团 / 腾讯 / 知乎 / vivo / 小米(feishu) |
| ❌ **URL 搜索失效** | 3 | 阿里 / 拼多多 / 滴滴 |
| 🏠 **校招子站（需站内搜）** | 6 | 京东 / 华为 / 理想 / 得物 / 小红书 / 小鹏 |

**重要**：之前 v1/v2 的链接**大量瞎写**——以为 `?keywords=X` 在所有公司都有效。Playwright 实测证明**可用的 8 家**，且**部分公司需要用 project ID / functionsids 代替关键词**。

## 🎯 v12 调试所有公司的总结

| 公司 | 实测状态 | 可用 URL 或原因 |
|---|---|---|
| 字节 | ✅ | `?keywords=X&project=7525009396952582407,7621018151002507573` |
| 美团 | ✅ | `/web/position?hiringType=4_1&keyword=X` |
| 腾讯 | ✅ | `?keyword=X` |
| 知乎 | ✅ | `#/jobs?keyword=X` |
| vivo | ✅ | `/home` (前端 JS 搜索) |
| 蔚来 | ✅ | `?keyword=X` (飞书系) |
| 小鹏 | ✅ | `?keyword=X` (飞书系) |
| 理想 | ✅ | `?project_id=4&functionsids=1` (函数 ID, 不是关键词) |
| 滴滴 | ✅ | `#/jobs?project=2027` (项目筛代替关键词) |
| 阿里 | 🏠 | talent.taotian.com 是项目入口 |
| 拼多多 | 🏠 | careers.pddglobalhr.com/campus/grad (v17 新域名, 22 岗位) |
| 得物 | 🏠 | Moka URL 404, dewu.com/career 是营销页 |
| 小红书 | 🏠 | URL 参数被忽略 |
| 大疆 | ✅ | `apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=X` (Moka) |
| 百度 | ✅ | `talent.baidu.com/jobs/list?projectType=X` (SSR 项目码筛) |
| 百度 | 🏠 | talent.baidu.com 反爬 |
| 京东 | 🏠 | URL 参数被忽略 |
| 华为 | 🏠 | 强制登录 uniportal.huawei.com |
| 小米 | ✅ | `xiaomi.jobs.f.mioffice.cn/campus?keywords=X` (v16飞书) |
| OPPO | ✅ | 完整校招系统, 但 2026 应届未启动 |
| 快手 | ✅ (项目筛) / 🏠 (类目码) | `?recruitSubProjectCodes=...` 真过滤；`?keyword=X` 已失效 (v18) |

## 🚪 v12 调试方法总结

**调一家公司的 URL 过滤能力**（v11 / v12 反复用的方法）:
1. Playwright 打开招聘主页
2. 看 body 里含什么 (一般是“招聘项目入口”/“项目”类别/“招聘项目名称”)
3. 找页面能点击的元素 (“应届校招” tab / “算法与软件” 分类)
4. 点击后看 URL 怎么变 → 抽参数 (美团 `hiringType=4_1` / 理想 `functionsids` / 滴滴 `project=2027`)
5. 带关键词的 URL 如果会被忽略 → 改用项目筛 / 分类 ID / 项目 ID

## 🆕 v20 百度校招实测

**项目名：AIDU（百度版 Top Seed）** —— 人才专项计划

URL 模板（SSR 项目码筛）：
- **默认 157 岗**：<https://talent.baidu.com/jobs/list>
- **校招项目=1（145 岗）**：<https://talent.baidu.com/jobs/list?projectType=1>
- **AIDU 项目=3（11 个顶级 AI 岗）**：<https://talent.baidu.com/jobs/list?projectType=3> ⭐
- **管培生项目=4（12 个）**：<https://talent.baidu.com/jobs/list?projectType=4>
- **实习生（399 岗）**：<https://talent.baidu.com/jobs/list?recruitType=INTERN>

**AIDU 11 个顶级岗位**（人才专项）：大模型算法 / 多模态算法 / AI 异构计算 / 语音大模型 / 大模型 Infra / 智能体算法 / Agent 应用全栈 / 基础模型架构师 / 端到端系统架构师 / 视觉-语言模型架构师。

**v20 SSR 返回的项目数据**：
```json
window.__INITIAL_DATA__ = {
  "listData": {
    "keyWord": "",                  // ⚠️ URL 参数被忽略
    "projectType": "3",             // ✅ 项目码生效
    "recruitType": "GRADUATE",
    "postList": [1=技术, 2=产品, 13=政企, 14=销售, 15=综合],
    "workPlaceList": [1100=北京, 3100=上海, 4403=深圳, ...],
    "graduateProjectList": [1=校招, 3=AIDU, 4=管培],
    "total": 11,                    // AIDU 真实总数
    "listDetailData": [...]         // 11 个岗位 全部 SSR 渲染
  }
}
```

> 🚨 **属性设定**：SSR 返窗口内嵌 JSON，但 `keyWord / workPlace / postType` 参数被 SSR 忽略，只有 `projectType / recruitType` 生效。位置/关键词篏必须进站内点类目。

## 🆕 v19 大疆校招实测

**项目名：「2027 拓疆者」校园招聘**（2026.6.25 启动，招 2027 届应届）

URL 模板（**Moka hash 路由**）：
- **校招全职位（138 岗）**：<https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs>
- **算法类（54 岗）**：<https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E7%AE%97%E6%B3%95>
- **大模型（6 岗）**：<https://apply.careers.dji.com/campus-recruitment/dji/143359#/jobs?keyword=%E5%A4%A7%E6%A8%A1%E5%9E%8B>
- **Moka Project ID**: 143359 （社会招聘是 170070）

**DJI 独有算法方向**（3 个城市：北京 / 上海 / 深圳）：
- SLAM 算法工程师（3 岗）
- GNSS 定位算法工程师（3 岗）
- 端到端决策规划算法工程师（3 岗）
- 多模态空间感知算法工程师（3 岗）
- 图传 AI 算法工程师（上海）
- 世界模型算法工程师（北京）
- 激光雷达传感器算法工程师（深圳）
- 计算机视觉算法工程师（2 岗）
- 图像算法工程师（2 岗）
- 多模态大模型算法工程师（6 岗）
- 大模型推理部署算法工程师（6 岗）

> 🎯 **DJI 推荐**: 如果你做 SLAM / 定位 / 感知 / 自主导航 / 大模型部署，DJI 是国内为数不多在 **无人机 + 机器人 + 自动驾驶** 三栈都领先的公司。

## 🆕 v18 快手校招重测

v14 里说的 `?keyword=X` 有效是错的，到 v18 **关键词已全部被忽略**。但发现了更详尽的过滤体系：

**项目码字典**（2027 应届使用）：
| 项目代码 | 项目名 |
|---|---|
| `20271779425607` | **2027 应届生** (74 岗位, 全为「快Star」人才计划) |
| `20271772783534` | 2027 实习 |
| `20261749721165` | 2026 应届生 |
| `20261707035672` | 2026 实习 |

**类目码字典**（74 个 2027 应届岗位按类目码聚合）：

| 类目码 | 类目 | 岗位数 | 顶级岗位 |
|---|---|---|---|
| J1013 | 大模型 Infra / 推理引擎 / GPU | 14 | 基础大模型推理引擎、推荐大模型训练引擎、混合云 AI 推理 |
| J1020 | 安全 / 分布式 / AI Infra | 12 | 安全工程师-Agentic AI、AI Infra 工程师、大模型推理优化 |
| J1007 | 多模态 / CV / 视频 / AIGC | 12 | 音视频大模型、多模态大模型 Keye、视频生成 |
| J1005 | **推荐** | 10 | 直播推荐、推荐大模型 OneRec、社交生成式推荐 |
| J1001 | 大模型算法 / Agent / RL | 8 | 具身智能、Agent 智能创作、用户画像、强化学习 |
| J1004 | 搜索 | 4 | AI 搜索、多模态搜索、搜索大模型 |
| J1006 | 广告 | 4 | 广告 AI、广告 Agent、广告大模型 |
| J1011 | 音视频体验 / 视频编码 | 4 | 智能编码、生成式视频编码 |

**4 个工作地**：北京 72 / 上海 14 / 深圳 14 / 杭州 12 （一岗位可投多个城市）

**准确做法**：

1. 打开 <https://campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271779425607>
2. **不能用 `?keyword=`**，会被忽略
3. 站内左侧栏「职位类别」复选框中点类目即可（前端 JS 本地过滤，不改 URL）
4. 「招聘项目」可选「快Star」人才计划

> 🚨 **v14 的错误结论**: 当时报告「`?keyword=推荐` 返 18 个」实际上是错的——v18 三次测试都是同样 74 个全量清单。重测尽量不要依赖很久之前的结论。

## 🆕 v17 拼多多新域名 + 完整 22 岗位列表

拼多多校招已迁移到**新域名**：`careers.pddglobalhr.com`（旧 `careers.pinduoduo.com` 301 跳转）。

- **校招主页**：<https://careers.pddglobalhr.com/campus/grad>
- **实习生招聘**：<https://careers.pddglobalhr.com/campus/intern>
- **URL 搜索失效**：`?keyword=` 被忽略，需进站内点类目筛
- **站内筛**：项目（云弧计划/技术专场/管培生...）× 类别（技术/产品/设计...）× 标签（紧缺/人才专项）
- 当前 **22 个** 2026 校招岗位

**重点「云弧计划」项目**（拼多多核心算法岗，人才专项）：
- [AI Infra 研发工程师](https://careers.pddglobalhr.com/campus/grad) — 上海
- [大模型算法工程师](https://careers.pddglobalhr.com/campus/grad) — 上海

**技术专场其他算法岗**（站内点「技术」）：
- AI Agent 研发工程师 / 算法工程师 / 服务端研发工程师 / 客户端 / Web 前端 / 数据分析师 / 安全工程师

> 🚨 **PDD 校招基本 all in 上海**，极少数管培生在河北雄安。

## 🆕 v16 小米飞书系统实测

小米校招真实投递系统是**飞书（mioffice）**，不是 `hr.xiaomi.com/campus/list`（那个 2018 年就过期了）。

- **飞书投递入口**：<https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR>
- **URL 模板**：`?keywords={方向}` 真实有效 ✅
- **招聘项目**：2026届春季校招 / 秋季校招 / 实习生 / 境外校招
- **职能分类**：软件研发类 / 硬件研发类 / 芯片类 / 运维类 / 产品类 / 运营类 / 市场类 / 职能类 / 销售类 / 商务类
- 算法岗归类在「软件研发类」下
- 当前 55 个岗位（2026 春季校招已近尾声，主要是 2027 届实习）

**热门算法方向**（直接在 URL 后加 `&keywords=方向`）：
- [推荐](https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E6%8E%A8%E8%8D%90)
- [大模型](https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E5%A4%A7%E6%A8%A1%E5%9E%8B)
- [自动驾驶](https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6)
- [语音](https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%AF%AD%E9%9F%B3)
- [NLP](https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=NLP)
- [计算机视觉](https://xiaomi.jobs.f.mioffice.cn/campus/?spread=J7NS6YR&keywords=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89)

**小米独有方向**：小爱同学 / 端侧 AI / 手机影像 / 自动驾驶 — 其他大厂少。

## 🆕 v14 新增 12 家中型企业

| 公司 | URL | 备注 |
|---|---|---|
| 快手校招 | `campus.kuaishou.cn/recruit/campus/e/#/campus/jobs?recruitSubProjectCodes=20271779425607` | 2027 届应届 74 岗，0 实习 |
| 携程 | `campus.ctrip.com` | 应届校招 + 留用实习 |
| 360 | `campus.360.cn` | 2026 全球 + 算法快速通道 |
| 虎牙 | `hr.huya.com` | 直播 |
| 鹰角 | `career.hypergryph.com` | 明日方舟母公司 |
| Keep | `hr.keep.com` | 运动健康 + AI |
| 飞书 | `www.feishu.cn/jobs` | 字节系 |
| 元戎启行 | `app.mokahr.com/apply/deeproute` | Moka 自动驾驶 |
| 网易 | `campus.163.com` | 163 |
| 网易有道 | `hr.youdao.com` | 有道 |
| 用友 | `career.yonyou.com` | 企业软件 SaaS |
| 猿辅导 | `hr.yuanfudao.com` | 教育 |

**美团系共享 URL**（v14 发现）: `zhaopin.meituan.com/web/position?hiringType=4_1&keyword=X` 同时适用于大众点评 / 猫眼 / 美团酒旅。

## 🆕 v15 新增 7 家

| 公司 | 行业 | URL | 备注 |
|---|---|---|---|
| 网易互娱 | 游戏 | `game.campus.163.com` | 阴阳师公测校招, body=628 |
| 三七互娱 | 游戏 | `zhaopin.37.com/?c=campus&a=index` | 含 AI类 / 游戏研发 / 技术开发 |
| 西山居 | 游戏 | `job.seasungames.cn/campus` | 剑网3/解限机, 训练营+应届+实习 |
| 叠纸 | 游戏 | `papegames.com/career` | 无限暖暖/恋与制作人 |
| 深信服 | 安全 | `hr.sangfor.com/campuszp` | 校招入口 + X-STAR 顶尖人才 |
| 摩尔线程 | 芯片/GPU | `mthreads.com/career` | 信创 GPU, 营销主页 |
| 阿里健康 | 医疗 | `alihealth.cn/career` | 阿里系, 加入我们 |

## 🎯 v9/v10 实习过滤关键发现

打开任意公司的招聘页面，搜索方向词后，**结果里通常混有 30-50% 的实习岗**。

实测后找到的**实习过滤方案**：

| 公司 | URL 模板 | 实习占比 |
|---|---|---|
| 字节跳动 | `?keywords=X&project=7525009396952582407,7621018151002507573` | ✅ 0% |
| 美团 | `/web/position?hiringType=4_1&keyword=X` | ✅ 0% (v11 发现) |
| 腾讯 | `?keyword=X` (默认就是校招) | ✅ 0% |
| 知乎 | `#/jobs?keyword=X` (默认就是校招) | ✅ 0% |
| vivo | `/home` (默认就是校招) | ✅ 0% |

**字节的 2 个正式校招项目 ID**：
- `7525009396952582407` — Seed 大模型人才校招 (正式)
- `7621018151002507573` — 2027 届 Seed 大模型人才校招

**美团的应届校招项目 ID**：`hiringType=4_1` (= 应届生校招项目, 排除实习)
- 注: NLP 方向必须搜"自然语言", 搜"NLP"返 0

**v11 突破**: v10 试了 12 种美团 URL 参数都过滤不掉实习。点击"应届校招" tab 后抓到 URL 变成 `?hiringType=4_1`, 这个参数才是过滤实习的关键。

## 📂 目录

| 文件 | 内容 |
|---|---|
| [data/01-cn-tech.md](./data/01-cn-tech.md) | 18 家公司完整实测（字节/美团/腾讯/知乎/vivo + 阿里/拼多多 + 阿里系/百度/京东/华为/小米/理想/得物 + 大疆/小红书/OPPO/小鹏 + AI 独角兽） |

## 🔍 v8 实测明细

### ✅ URL 搜索真实有效 (5 家)

| 公司 | URL 模板 | 实测证据 |
|---|---|---|
| 字节 | `?keywords=X` | 搜"推荐"/"NLP"/"LLM" 返回对应岗位 |
| 美团 | `?keyword=X` | 搜"推荐"/"NLP" 返回对应岗位 |
| 腾讯 | `?keyword=X` | 搜"推荐" 返回"算法-推荐算法方向" |
| 知乎 (Moka) | `#/jobs?keyword=X` | 搜"推荐" 返回"推荐策略产品"等 |
| vivo | `/home` (URL 不变) | 搜"推荐" 返 33 个, 搜"NLP" 返 16 个 (前端 JS 搜索) |

### ❌ URL 搜索失效 (4 家)

| 公司 | 实测现象 | 正确做法 |
|---|---|---|
| 阿里 | `?keywords=推荐` 跳默认 20 个岗位 | 进首页用站内搜 |
| 拼多多 | `?keywords=推荐` 无过滤 | 进首页用站内搜 |
| 蔚来 | `?keyword=推荐` 无过滤 | 进首页用站内搜 |
| 滴滴 | `?keyword=推荐` 无过滤 | 进首页用站内搜 |

### 🏠 校招子站 / 营销页 (9 家)

| 公司 | 实测状态 | 推荐链接 |
|---|---|---|
| 百度 | 完全 JS 渲染 (body_len=0) | 用主站 `talent.baidu.com` |
| 京东 | 有搜索框但 fill 超时 | `campus.jd.com` |
| 华为 | 主页无 input | `career.huawei.com` |
| 小米 | 主页即结果页 | `hr.xiaomi.com/campus/list` |
| 理想 | 有搜索框但 fill 超时 | `lixiang.com/recruit` |
| 得物 | Moka 404 | 改用 BOSS直聘 |
| 大疆 | 校招主页, 需点"查看在招职位" | `we.dji.com/zh-CN/campus/` |
| 小红书 | 校招项目入口, 需点"立即投递" | `campus.xiaohongshu.com/positions` |
| OPPO | 校招子站, 需向下滚动 | `careers.oppo.com/university/oppo/` |
| 小鹏 | 主页是车介绍页 (营销页) | join.html 是营销 |
| 快手 | 主页是校招宣传页 | `campus.kuaishou.cn/` |

## 💡 给用户的使用建议

**优先级**：
1. **✅ 优先用这 5 家**：字节 / 美团 / 腾讯 / 知乎 / vivo 的链接（URL 搜索真实有效）
2. **🏠 这 9 家**：进首页 → 用站内搜索框搜方向词
3. **❌ 这 4 家**：放弃 URL 搜索，直接进首页

**关键经验**：
- 不要相信一个看起来正常的 URL 真的过滤了关键词
- 阿里 / 拼多多 / 蔚来 / 滴滴的 `?keyword=X` 是无效的
- vivo 的 URL 不变但 body 内容确实过滤了——这是前端 JS 搜索

## 📊 测试方法

```python
# 每家公司的实测流程:
1. Playwright 启动 Chromium
2. 打开招聘主页
3. 找搜索框 (多种 selector: type=search, placeholder 含"搜索")
4. 输入"推荐" / "NLP" 等关键词
5. 按 Enter
6. 等待 3 秒
7. 检查:
   - URL 是否变了
   - body 是否含该关键词
   - body 是否含"算法"
   - 截图保留
```

## 📊 v8 vs v2 改进

| 维度 | v2 | v8 |
|---|---|---|
| 链接来源 | curl HEAD 验 200 | Playwright 实测 + 验证内容 |
| 字节/美团/腾讯 | ✅ | ✅ (实测) |
| 知乎 (Moka) | ❌ 瞎写 | ✅ 实测 |
| vivo | ⚠️ | ✅ 新发现 URL 搜索有效 |
| 阿里/拼多多/蔚来/滴滴 | ⚠️ 瞎写 | ❌ 实测无效, 标注为"需站内搜" |
| OPPO/大疆/小红书 | ⚠️ 瞎写 | ✅ 实测找到校招子站 |
| 小鹏/理想/快手 | ⚠️ 瞎写 | ❌ 主页是营销页, 实测 |

## ⚠️ 数据局限

- **测试关键词有限**：只测了"推荐"和"NLP"，其他关键词（如"LLM"、"CV"）可能不一样
- **测试环境**：用 Playwright headless 模式，可能与真实浏览器有差异
- **测试时间**：2026-07-07，校招网站结构可能随时变化

## 下一步

- 用 Playwright 实测更多关键词（LLM / CV / 自动驾驶感知等）
- 把"实测数据"沉淀为结构化数据（JSON / CSV）便于程序化使用
- 添加定期自动重测脚本（检测链接是否失效）