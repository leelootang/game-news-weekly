# Selection Decisions｜2026-08-14_to_2026-08-16

- 报告类型：周末报（日报式逐条判断）；行业阈值 E×R+M ≥ 7。
- 双周历史窗口：2026-07-31 至 2026-08-13；105 条历史行业记录。
- 卡片曝光去重：腾讯Q2、墨犬停业、尘白制作人离职均命中 card_exposed=true，按 repeat_only 排除；《镇邪人》历史卡片未曝光但出现榜单与投放实质状态变化，按 material_update 入选；本期 card_carryover=无。
- 维度覆盖自检：国内移动 9 张 / 国产产品与人才 10 张 / 市场数据 6 张 / 并购 2 张 / 平台政策 3 张 / 档期变动 6 张 / 资本组织 9 张 / 海外重大 8 张。
- AI反扫：254 条行业新闻与16条AI趋势均已反扫；3条直接作用类入选，通用模型更新因缺少游戏迁移链排除。
- 产品日历漏挂反查：已反扫 industry_news 与 release_calendar 全量输入；同步脚本按多源可发布前缀选出2条，未达到4条上限。
- 深度交接：周末报不消费周五人工 selection；D001 按 R/I/E/C=11 自动入选。

## 行业新闻 E×R+M 打分记录

- I001｜事件3×相关3+钩子2 = 11｜include
- I002｜事件3×相关3+钩子2 = 11｜include
- I003｜事件3×相关3+钩子1 = 10｜include
- I004｜事件2×相关3+钩子2 = 8｜include
- I005｜事件3×相关2+钩子2 = 8｜include
- I006｜事件2×相关3+钩子1 = 7｜include
- I007｜事件2×相关3+钩子1 = 7｜include
- I101｜事件3×相关3+钩子1 = 10｜exclude
- I102｜事件2×相关3+钩子1 = 7｜exclude
- I103｜事件3×相关3+钩子1 = 10｜exclude
- I104｜事件2×相关2+钩子2 = 6｜exclude
- I105｜事件3×相关1+钩子2 = 5｜exclude
- I106｜事件2×相关2+钩子1 = 5｜exclude
- I107｜事件2×相关2+钩子1 = 5｜exclude
- I108｜事件2×相关2+钩子1 = 5｜exclude
- I109｜事件2×相关2+钩子2 = 6｜exclude
- I110｜事件3×相关3+钩子1 = 10｜exclude
- I111｜事件0×相关3+钩子1 = 1｜exclude
- I112｜事件0×相关3+钩子2 = 2｜exclude

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001｜多家媒体称信宸资本拟以超15亿美元收购灵犀互娱，交易尚待官方确认 | include | industry_news | 国内成熟游戏资产的重大收购信号，多源同日覆盖且直接影响国产SLG与卡牌团队归属。 |
| I002｜《湮灭之潮》举行首次大规模线下试玩，研发团队已扩至150人 | include | industry_news | 国产在研产品完成首次大规模玩家试玩并披露团队与研发阶段，多源形成强窗口钩子。 |
| I003｜快手与星竞威武达成一年战略合作，电竞战队与主播资源将进入平台生态 | include | industry_news | 国内平台与电竞集团的明确战略合作，覆盖直播、赛事、主播与商业化链路。 |
| I004｜美国参议院启动Roblox儿童安全调查，要求8月底前提交平台记录 | include | industry_news | Roblox为最高关注主体，联邦调查构成平台治理与合规的实质新阶段。 |
| I005｜美泰组建近300人全球游戏工作室，杭州团队参与《UNO Wild》等自研产品 | include | industry_news | IP公司完成组织整合并建立中美约300人自研团队，对移动IP产品全球化有明确迁移点。 |
| I006｜掌趣《Titan Rush: Survival》双端下载破320万，累计内购收入超410万美元 | include | industry_news | 国内厂商海外SLG出现可核验的下载、收入和区域榜单数据。 |
| I007｜三七互娱《镇邪人》一度冲入微信小游戏畅销榜前三，近期回落至第12名 | include | industry_news | 相对历史榜单新入事实，本期新增Top3后回落第12及日均投放规模，构成可验证状态变化。 |
| I101｜腾讯第二季度游戏业务数据的窗口内重复报道 | exclude | industry_news | 日报已完成卡片曝光，本期未出现新的财务周期或产品状态。 |
| I102｜北京墨犬科技停业清盘事件的窗口内转载 | exclude | industry_news | 同一停业清盘事件已在日报卡片曝光，本期只有转载与背景补充。 |
| I103｜《尘白禁区》发行制作人离职信息的重复讨论 | exclude | industry_news | 周末报与周报均已卡片曝光，本期社区帖子没有新的任职状态。 |
| I104｜Netflix关闭Night School与Moonloot并继续削减游戏岗位 | exclude | industry_news | 工作室关闭事件重要但与重点市场迁移较弱，E2×R2+M2=6，未达7分。 |
| I105｜2K在温哥华成立Small Axe Studios开发新体育IP | exclude | industry_news | 新工作室成立但对移动与国内竞争格局迁移较弱，E3×R1+M2=5。 |
| I106｜《Arc Raiders》第二季度收入与销量更新 | exclude | industry_news | 数据具体但与重点市场和优先赛道迁移有限，E2×R2+M1=5。 |
| I107｜Niko Partners发布印度游戏市场规模预测 | exclude | industry_news | 市场数据成立但当前迁移点较弱且为单源，E2×R2+M1=5。 |
| I108｜亚马逊归还《失落方舟》等MMO发行权 | exclude | industry_news | 发行权变化成立，但以海外PC MMO为主，E2×R2+M1=5。 |
| I109｜多人旅行游戏窗口内首发收入报道 | exclude | industry_news | 产品表现有钩子但主体与长期迁移证据不足，E2×R2+M2=6。 |
| I110｜莉莉丝《小冰冰斗蛐蛐》不删档测试的晚到分析 | exclude | industry_news | 测试发生在8月10日、早于本期窗口，窗口内材料未提供新的状态变化。 |
| I111｜祖龙娱乐上半年亏损预告与研发投入说明 | exclude | industry_news | 缺少相对一致预期或公司指引的异常比较基准，按财报例外排除。 |
| I112｜吉比特上半年业绩与分红报道 | exclude | industry_news | 常规财报与同比变化，不满足财报例外。 |
| A001｜《洛克王国：世界》上线AI阵容教练，PVP激活率提升20% | include | ai_news | 直接作用于PVP教学与激活，并披露准确率、知识库和业务结果。 |
| A002｜Catfly.ai用20个智能体支撑两人团队月产千款轻量游戏，验证瓶颈转向市场决策 | include | ai_news | AI已直接覆盖游戏美术、代码、适配、测试和发行决策。 |
| A003｜Saber为《Rideshare Stimulator》补充Steam AI披露，实验模式成本反而高于不用AI | include | ai_news | AI对话与音乐已进入产品，且披露额外人员和成本结果。 |
| A101｜Gemini 3.7 Flash发布与用户扩围 | exclude | ai_news | 没有来源证明其已进入具体游戏环节，迁移链条过泛。 |
| A102｜Cursor被SpaceX收购的重复采集 | exclude | ai_news | 交易核心不在游戏应用，缺少明确游戏迁移路径。 |
| A103｜开源模型与价格竞争资讯 | exclude | ai_news | 属于通用模型参数、价格或生态更新，无法形成具体游戏迁移链。 |
| C001｜《原神》7.0强制剧情开图与移动端负载上升，玩家争论探索节奏是否被打断 | include | community_discourse | 窗口内持续出现新回复，触发点、争议逻辑和时间线完整。 |
| C002｜《大侠立志传》新作被指更换主控并移除结缘，玩家担心前作核心自由度被削弱 | include | community_discourse | 本期新帖形成可命名事件，并呈现对立意见。 |
| C101｜《战舰少女R》头像被指与《碧蓝航线》立绘相似 | exclude | community_discourse | 单帖重复采集，缺少官方回应或可核验的新进展。 |
| C102｜《崩坏：星穹铁道》角色立绘相似争议 | exclude | community_discourse | 主张主要来自玩家对比，证据链不足且未出现窗口内后续。 |
| C103｜《异环》反派角色入池与同居机制讨论 | exclude | community_discourse | 同一帖多日重复采集，触发事实与官方设计边界仍不清楚。 |
| C104｜《王者荣耀世界》第二赛季延期讨论 | exclude | community_discourse | 帖子证据不足以确认官方延期口径，未进入正文。 |
| C105｜《阴阳师》维权声明引发相似玩法争论 | exclude | community_discourse | 单帖主要复述诉讼立场，玩家争议机制不够完整。 |
| C106｜《重返未来：1999》插图相似争议 | exclude | community_discourse | 缺少可靠的权利方或官方后续，无法越过玩家指控。 |
| C107｜《烟雨江湖》角色序列被玩家破解讨论 | exclude | community_discourse | 单帖技术主张缺少复核来源，不能写成已证实机制。 |
| C108｜《和平精英》赛事选手食物中毒讨论 | exclude | community_discourse | 主要为同帖重复采集，缺少官方时间线与处理结果。 |
| C109｜未成年人在《三国杀移动版》大额充值引发责任争论 | exclude | community_discourse | 事件具备讨论价值，但本期更优先保留直接关联产品设计和探索体验的两条舆论。 |
| D001｜《Iron Nest》三天售出25万份：机械操作钩子如何串起短视频、Demo与新品节 | include | deep_analysis | 单篇高质量newsletter提供完整销量、愿望单、Demo与渠道转化链。 |
| release-candidate-001｜2026-08-15 删档测试 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-002｜2026-08-16 正式上线 | include | release_calendar | 多源候选按事件类型×来源强度+重点公司加分排序进入报告上限 |
| release-candidate-003｜2026-07-23 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-004｜2026-08-12 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-005｜2026-08-14 新品首次曝光 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-006｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-007｜2026-08-19 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-008｜2026-09-10 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-009｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-010｜2026-11-19 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-011｜2026-08-14 公测 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-012｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-013｜2026-08-12 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-014｜2026-08-01 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-015｜2026-04-01 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-016｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-017｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-018｜2026-08-20 公开测试 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-019｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-020｜2026-08-15 公测 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-021｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-022｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-023｜2026-09-02 正式上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-024｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-025｜2026-12-03 新品定档 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-026｜2026-08-14 新品首次曝光 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-027｜2026-08-15 新品首次曝光 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-028｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-029｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-030｜2026-08-14 公开测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-031｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-032｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-033｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-034｜2026-08-14 不删档测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-035｜2026-08-14 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-036｜2026-08-14 删档测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-037｜2026-08-14 不限量测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-038｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-039｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-040｜2026-08-15 删档测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-041｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-042｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-043｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-044｜2026-08-15 不限量测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-045｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-046｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-047｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-048｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-049｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-050｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-051｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-052｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-053｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-054｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-055｜2026-08-15 限量测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-056｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-057｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-058｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-059｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-060｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-061｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-062｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-063｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-064｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-065｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-066｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-067｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-068｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-069｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-070｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-071｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-072｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-073｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-074｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-075｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-076｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-077｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-078｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-079｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-080｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-081｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-082｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-083｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-084｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-085｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-086｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-087｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-088｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-089｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-090｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-091｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-092｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-093｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-094｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-095｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-096｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-097｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-098｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-099｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-100｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-101｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-102｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-103｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-104｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-105｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-106｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-107｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-108｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-109｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-110｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-111｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-112｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-113｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-114｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-115｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-116｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-117｜2026-08-15 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-118｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-119｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-120｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-121｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-122｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-123｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-124｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-125｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-126｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-127｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-128｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-129｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-130｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-131｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-132｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-133｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-134｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-135｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-136｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-137｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-138｜2026-08-16 不限量测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-139｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-140｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-141｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-142｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-143｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-144｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-145｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-146｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-147｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-148｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-149｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-150｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-151｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-152｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-153｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-154｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-155｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-156｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-157｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-158｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-159｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-160｜2026-08-16 限量测试 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-161｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-162｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-163｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-164｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-165｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-166｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-167｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-168｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-169｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-170｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-171｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-172｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-173｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-174｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-175｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-176｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-177｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-178｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-179｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-180｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-181｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-182｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-183｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-184｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-185｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-186｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-187｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-188｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-189｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-190｜2026-08-16 正式上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-191｜2026-08-14 新品首次曝光 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-192｜2026-08-14 新品预下载 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-193｜2026-08-16 新品预下载 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-194｜2026-09-03 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-195｜2026-09-02 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-196｜2026-08-14 老品跨平台上线 | exclude | release_calendar | 单源不具备正文资格 |
| release-candidate-197｜2026-09-24 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-198｜2026-09-15 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
| release-candidate-199｜2026-10-22 老品跨平台上线 | exclude | release_calendar | 事件日期不在报告窗口 |
