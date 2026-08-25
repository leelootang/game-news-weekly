# Selection Decisions

- 卡片曝光去重：历史匹配项均已读取 card_exposed/card_rank/card_limit/card_exposure_source；本期3条 material_update、4条 repeat_only；无合格 card_carryover。
- 维度覆盖自检：国内移动 9 张 / 国产产品与人才 8 张 / 市场数据 10 张 / 并购 2 张 / 平台政策 4 张 / 档期变动 4 张 / 资本组织 3 张 / 海外重大 16 张。
- 产品日历漏挂反查：已反扫 industry_news 与 release_calendar 全量输入；95个节点全部 appearance_count=1，多源合格0个，正文0条。
- 行业新闻 E×R+M 打分记录：以下每条行业候选逐条写出“事件E×相关R+钩子M = 终分”；日报总分≥7方可入选，E=0一票否决。

| candidate | decision | target_section | reason |
| --- | --- | --- | --- |
| I001 | include | industry_news | 新品上线且命中策略/卡牌优先赛道，E3×R3+M1=10。 事件3×相关3+钩子1 = 10。 |
| I002 | exclude | industry_news | Roblox固定R=3且总分10，但唯一来源为snippet，按来源质量门禁排除。 事件3×相关3+钩子1 = 10。 |
| I003 | include | industry_news | 新品首次曝光且命中策略优先赛道，E3×R3+M1=10。 事件3×相关3+钩子1 = 10。 |
| I004 | include | industry_news | 新品正式进入EA且命中模拟经营优先赛道，E3×R3+M1=10。 事件3×相关3+钩子1 = 10。 |
| I005 | include | industry_news | 国内手游经营数据获两家媒体同日覆盖，E2×R3+M2=8。 事件2×相关3+钩子2 = 8。 |
| I006 | include | industry_news | RPG优先赛道重大档期由full-body来源支持，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I007 | include | industry_news | 国内PVP产品出现可核验的DAU实质更新，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I008 | include | industry_news | 国内厂商产品从前15进一步升至Top 10，构成实质状态变化，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I009 | include | industry_news | 国内PVP手游披露新的榜单与用户结构，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I010 | include | industry_news | 国产产品披露新的累计销量里程碑，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I011 | include | industry_news | 国内小游戏平台政策发生结构性变化，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I012 | include | industry_news | Roblox固定R=3，平台能力出现实质升级，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I013 | include | industry_news | PVP优先赛道披露重要销量数据与中国市场迁移点，E2×R3+M1=7。 事件2×相关3+钩子1 = 7。 |
| I014 | exclude | industry_news | 卡牌优先赛道总分7，但唯一来源为snippet，按来源质量门禁排除。 事件2×相关3+钩子1 = 7。 |
| I015 | exclude | industry_news | 即时游戏资产收购总分7，但唯一来源为snippet，按来源质量门禁排除。 事件3×相关2+钩子1 = 7。 |
| I101 | exclude | industry_news | 历史卡片已展示公测早期经营数据，本期没有实质新状态。 事件2×相关3+钩子1 = 7。 |
| I102 | exclude | industry_news | 同一事件已进入周末报订阅卡片，本期仅换来源复述。 事件2×相关3+钩子1 = 7。 |
| I103 | exclude | industry_news | 远征系统重做已在周末报卡片展示，无新增状态。 事件2×相关3+钩子1 = 7。 |
| I104 | exclude | industry_news | 首次测试已进入历史卡片，本期主要补充体验背景。 事件3×相关3+钩子1 = 10。 |
| I105 | exclude | industry_news | 海外PC工作室资本动作多源覆盖，但与移动及优先赛道迁移较弱，总分5。 事件3×相关1+钩子2 = 5。 |
| I106 | exclude | industry_news | 平台结构数据有迁移价值但总分5。 事件2×相关2+钩子1 = 5。 |
| I107 | exclude | industry_news | 全球移动数据具迁移点但总分5。 事件2×相关2+钩子1 = 5。 |
| I108 | exclude | industry_news | 命中卡牌赛道但4月发售数据缺少当日钩子，总分6。 事件2×相关3+钩子0 = 6。 |
| I109 | exclude | industry_news | 固定R=3且多源，但事件以旧更新复盘为主，总分5。 事件1×相关3+钩子2 = 5。 |
| I110 | exclude | industry_news | 国内在研团队信号已成卡，但执行标的较小且未证明项目状态变化，总分4。 事件1×相关3+钩子1 = 4。 |
| I111 | exclude | industry_news | 海外展会扩张与业务迁移较弱，总分3。 事件2×相关1+钩子1 = 3。 |
| I112 | exclude | industry_news | 纯赛事结果与俱乐部排名，E=0。 事件0×相关3+钩子1 = 1。 |
| I113 | exclude | industry_news | 多源但与移动及优先赛道迁移弱，总分4。 事件2×相关1+钩子2 = 4。 |
| I200 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I201 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I202 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I203 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I204 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I205 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I206 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I207 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I208 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I209 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I210 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I211 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I212 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I213 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I214 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I215 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I216 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I217 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I218 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I219 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I220 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I221 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I222 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I223 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I224 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I225 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I226 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I227 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I228 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I229 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I230 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I231 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I232 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I233 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I234 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I235 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I236 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I237 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I238 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I239 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I240 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I241 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I242 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I243 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I244 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I245 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I246 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I247 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I248 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I249 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I250 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I251 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I252 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I253 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I254 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I255 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I256 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I257 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I258 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I259 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I260 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I261 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I262 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I263 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I264 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I265 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I266 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I267 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I268 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I269 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I270 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I271 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I272 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I273 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I274 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I275 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I276 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I277 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I278 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I279 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I280 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I281 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I282 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I283 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I284 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I285 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I286 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| I287 | exclude | industry_news | E0×R0+M0=0；适用批量E=0类别，本条按独立来源留痕。 事件0×相关0+钩子0 = 0。 |
| A001 | include | ai_news | AI已经直接作用于小游戏生成、分发与内容平台运营。 |
| A002 | include | ai_news | AI素材直接影响游戏产品口碑与上线后的内容修订。 |
| A003 | include | ai_news | AI训练数据治理直接作用于游戏直播平台和创作者运营。 |
| A101 | exclude | ai_news | 同一事件已进入2026-08-21_to_2026-08-23周末报AI分区，本期无新增模型或部署状态。 |
| A102 | exclude | ai_news | 迁移价值存在，但缺少游戏研发的直接采用事实，优先级低于三条直接作用类。 |
| A103 | exclude | ai_news | 泛科技评论，未形成来源支持的具体游戏迁移链。 |
| A104 | exclude | ai_news | 硬件参数缺少具体游戏环节与落地事实。 |
| C001 | include | community_discourse | 当前窗口新发生、触发点与争议逻辑明确。 |
| C002 | include | community_discourse | 8月24日新建讨论，时间线与对立意见完整。 |
| C101 | exclude | community_discourse | 同一事件已进入2026-08-21_to_2026-08-23周末报，本期新增回复没有规则变化。 |
| C102 | exclude | community_discourse | 帖主主动求证且窗口内无可核验的原始截图或官方机制说明。 |
| C103 | exclude | community_discourse | 事件与官方补发调整均发生在8月19至20日，本期仅有延续回复。 |
| C104 | exclude | community_discourse | 8月7日事件在本期没有新增下架或回应状态。 |
| C105 | exclude | community_discourse | 单一动画细节争议缺少更完整产品影响与后续。 |
| C106 | exclude | community_discourse | 成本披露已是公测背景且本期没有新状态。 |
| C107 | exclude | community_discourse | 相关公测数据和一折券已进入周末报，本期没有新增官方方案。 |
| C108 | exclude | community_discourse | 单一作者后台口径无法验证，且讨论不足以形成完整事件。 |
| C109 | exclude | community_discourse | 普通美术展示，缺少可命名争议事件。 |
| C110 | exclude | community_discourse | 求证帖未形成可信事实链。 |
| C111 | exclude | community_discourse | 轻量彩蛋不构成舆论事件。 |
| C112 | exclude | community_discourse | 帖子始于8月21日且本期仅有零星延续回复。 |
| C113 | exclude | community_discourse | 非游戏事件。 |
| D001 | include | deep_analysis | R3/I3/E2/C3=11，平台政策事实充分，可解释分成、广告金与再投放之间的机制。 |
| release-candidate-001 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-002 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-003 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-004 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-005 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-006 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-007 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-008 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-009 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-010 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-011 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-012 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-013 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-014 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-015 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-016 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-017 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-018 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-019 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-020 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-021 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-022 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-023 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-024 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-025 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-026 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-027 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-028 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-029 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-030 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-031 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-032 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-033 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-034 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-035 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-036 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-037 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-038 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-039 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-040 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-041 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-042 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-043 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-044 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-045 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-046 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-047 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-048 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-049 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-050 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-051 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-052 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-053 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-054 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-055 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-056 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-057 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-058 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-059 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-060 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-061 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-062 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-063 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-064 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-065 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-066 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-067 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-068 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-069 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-070 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-071 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-072 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-073 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-074 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-075 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-076 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-077 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-078 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-079 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-080 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-081 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-082 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-083 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-084 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-085 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-086 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-087 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-088 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-089 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-090 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-091 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-092 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-093 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-094 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
| release-candidate-095 | exclude | release_calendar | 独立来源不足2个，未达到产品日历多源门槛。 |
