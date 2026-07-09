# job-pulse — 2026 校招算法岗情报站（实测版 v16）

> **v16：小米校招实测 → 飞书 mioffice 系统，URL keywords 搜索真实有效**
> **v15：添加 7 家游戏/安全/芯片/医疗公司**
> **v14：扩展 12 家中型企业 + 美团系共享 URL**
> **v13：发现 OPPO 完整校招系统 + 3 个调度 API**
> **实测日期**：2026-07-07
> **方法**：用 Playwright 启动 Chromium，对每家公司执行"打开主页 + 搜索方向词 + 验证 URL 是否生效 + body 是否真的过滤 + 验证是否含实习岗"

## 🎯 v8 实测核心结论

**18 家公司实测后**：

| 类型 | 数量 | 公司 |
|---|---|---|
| ✅ **URL 搜索真实有效** | 6 | 字节 / 美团 / 腾讯 / 知乎 / vivo / 小米(feishu) |
| ❌ **URL 搜索失效** | 3 | 阿里 / 拼多多 / 滴滴 |
| 🏠 **校招子站（需站内搜）** | 8 | 百度 / 京东 / 华为 / 理想 / 得物 / 大疆 / 小红书 / 快手 / 小鹏 |

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
| 拼多多 | 🏠 | career.pinduoduo.com 是营销页 |
| 得物 | 🏠 | Moka URL 404, dewu.com/career 是营销页 |
| 小红书 | 🏠 | URL 参数被忽略 |
| 大疆 | 🏠 | careers.dji.com 可访问但需点 "查看职位" |
| 百度 | 🏠 | talent.baidu.com 反爬 |
| 京东 | 🏠 | URL 参数被忽略 |
| 华为 | 🏠 | 强制登录 uniportal.huawei.com |
| 小米 | ✅ | `xiaomi.jobs.f.mioffice.cn/campus?keywords=X` (v16飞书) |
| OPPO | ✅ | 完整校招系统, 但 2026 应届未启动 |
| 快手 | 🏠 | campus.kuaishou.cn 营销页 |

## 🚪 v12 调试方法总结

**调一家公司的 URL 过滤能力**（v11 / v12 反复用的方法）:
1. Playwright 打开招聘主页
2. 看 body 里含什么 (一般是“招聘项目入口”/“项目”类别/“招聘项目名称”)
3. 找页面能点击的元素 (“应届校招” tab / “算法与软件” 分类)
4. 点击后看 URL 怎么变 → 抽参数 (美团 `hiringType=4_1` / 理想 `functionsids` / 滴滴 `project=2027`)
5. 带关键词的 URL 如果会被忽略 → 改用项目筛 / 分类 ID / 项目 ID

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