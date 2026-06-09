# Sources Used — 2026-05-28_to_2026-06-04

## 本地输入文件夹

- `news_data/industry_news/2026-05-28` … `2026-06-04`（8 天）
- `news_data/ai_trends/2026-05-28` … `2026-06-04`
- `news_data/release_calendar/2026-05-28` … `2026-06-04`
- `news_data/community_discourse/2026-05-28` … `2026-06-04`
- `news_data/deep_analysis/2026-05-28` … `2026-06-04`（缺 2026-05-31，已知缺口）
- `news_data/pc_rankings/2026-06-04`（本轮新采集的 Steam 官方周销量榜，record id `steamdb_rankings_periodic_2026-05-28_to_2026-06-04`）

## 抽取与中间文件

- 抽取汇总：`output/weekly/2026-05-28_to_2026-06-04/_intermediate/report_inputs_summary.md`（1237 条，0 失败）
- 索引：`_intermediate/report_inputs_index.md`
- 候选卡：`_intermediate/event_candidates.md`
- 取舍：`_intermediate/selection_decisions.md`

> 说明：source_id（S0001 等）对应 `report_inputs.jsonl` 记录；个别记录在 index.md 与 jsonl 间存在 1 位编号漂移，本映射以 jsonl 记录内容为准。

## Item Source Map

### steam 周榜

- steam 周榜 TOP15 + 新上榜 bullets —— `steamdb_rankings_periodic_2026-05-28_to_2026-06-04`｜`news_data/pc_rankings/2026-06-04/articles.jsonl`｜https://store.steampowered.com/charts/topselling/global ｜ 销量/营收来自 Gamalytic 估算；周榜取最近完整周 of 2026-05-26。

### 一、行业新闻

1. 腾讯SPARK2026发布会：42款游戏亮相，两项游戏AI技术压轴落地 —— S0001, S0085, S0035, S0018｜gamelook.com.cn / gcores.com / yystv.net｜http://www.gamelook.com.cn/2026/05/594077/
2. 微信小游戏MAU破5亿，PC端成为新增量窗口 —— S0006, S0003, S0004, S0044｜gamelook.com.cn / new.qq.com｜http://www.gamelook.com.cn/2026/05/594104/
3. 腾讯股价单日暴涨10.09%，催化剂为微信AI智能体原型测试完成 —— S0866｜gamelook.com.cn｜http://www.gamelook.com.cn/2026/06/594601/
4. Fortnite全球iOS回归首周340万下载，创八年新高 —— S0051｜gamesindustry.biz｜https://www.gamesindustry.biz/fortnites-global-ios-return-reportedly-reaches-34m-downloads-marking-an-eight-year-high
5. 《王者荣耀：世界》执行制作人李新平公测一月后离职 —— S0661, S0670, S0210｜youxituoluo.com / new.qq.com / cgames.com｜https://www.youxituoluo.com/534540.html
6. 网易《破碎之地》制作人吴晓创业，新作《逃离动物城》主打俯视角PVE搜打撤 —— S0676, S0757｜new.qq.com / 3839.com｜https://new.qq.com/rain/a/20260602A04YKU00
7. 腾讯《三角洲行动》招聘曝光UGC平台计划 —— S0471｜pocketgamer.biz｜https://www.pocketgamer.biz/tencent-reportedly-preparing-ugc-initiative-for-delta-force/
8. 灵犀《宗师之上》上线即爆，首次试水放置MMO品类 —— S0438, S1070｜gamelook.com.cn / cgames.com｜http://www.gamelook.com.cn/2026/06/594332/
9. 巨人《超自然行动组》出海日韩，日免费榜第3、韩第7 —— S0202｜gamelook.com.cn｜http://www.gamelook.com.cn/2026/05/594321/
10. 网易2026年Q1游戏收入同比增6.9%至约37亿美元 —— S0231｜gamesindustry.biz｜https://www.gamesindustry.biz/netease-reports-69-increase-in-games-revenue-to-37bn-during-q1
11. Block Blast（3亿MAU）突遭谷歌Play下架，同日恢复 —— S0234, S0239｜pocketgamer.biz｜https://www.pocketgamer.biz/hungry-studios-block-blast-no-longer-available-on-google-play/
12. Atari以最高3930万美元收购《Crossy Road》开发商Hipster Whale —— S0479, S0481, S0505｜mobilegamer.biz / pocketgamer.biz / gamedeveloper.com｜https://mobilegamer.biz/atari-acquires-crossy-road-maker-hipster-whale-for-an-initial-29-3m/
13. ESA 2026年报：美国2025年游戏消费607亿美元，移动为最大平台 —— S0884, S0899｜gamesindustry.biz / gamedeveloper.com｜https://www.gamesindustry.biz/esa-67-of-americans-played-video-games-for-more-than-an-hour-in-2025
14. Niko Partners：亚洲及MENA游戏市场2030年预计达1036亿美元 —— S0893｜pocketgamer.biz｜https://www.pocketgamer.biz/report-asia-and-mena-video-game-revenue-set-to-surpass-100bn-by-2030/
15. 抖音游戏白皮书：65.3%流水增量来自上线超一年的成熟产品 —— S0666｜youxichaguan.com｜https://youxichaguan.com/archives/197630
16. 欧洲移动游戏2025年全球营收75.3亿欧元（King委托报告） —— S0677, S0478｜gamesindustry.biz / pocketgamer.biz｜https://www.gamesindustry.biz/european-mobile-games-sector-generates-753bn-globally-in-2025
17. 神魔之塔宣传片实锤抄袭《鸣潮》，Madhead道歉 —— S0203｜gamelook.com.cn｜http://www.gamelook.com.cn/2026/05/594281/
18. 金山Q1游戏收入下滑22%，西山居推进"关停并转" —— S0204｜gamelook.com.cn｜http://www.gamelook.com.cn/2026/05/594299/

### 二、AI 新闻

1. 腾讯MagicDawn NDGI：全球首个跨平台神经动态全局光照，全面开源 —— S0001, S0028｜gamelook.com.cn / gcores.com｜http://www.gamelook.com.cn/2026/05/594077/
2. 腾讯"代号Craft"：自然语言输入即可生成可玩游戏 —— S0001, S0020｜gamelook.com.cn / youxichaguan.com｜http://www.gamelook.com.cn/2026/05/594077/
3. GDC 2026趋势报告：生成式AI采用上升，但落地标准仍有分歧 —— S1059｜gamelook.com.cn｜http://www.gamelook.com.cn/2026/06/594666/
4. 微信内嵌AI智能体完成原型测试，剑指小程序生态互通 —— S0866｜gamelook.com.cn｜http://www.gamelook.com.cn/2026/06/594601/

### 三、新游发布 / 产品日历

- 产品日历 - 崩坏：星穹铁道 —— S0547, S0545｜3839.com / 17173.com｜https://www.3839.com/ ｜本地证据：release_calendar 多源（3839 + 17173）
- 产品日历 - 鸣潮 —— S0285｜gematsu.com｜June 8；本地证据：release_calendar + community_discourse（CC001 同游戏）双覆盖
- 产品日历 - 宝可梦 Champions —— S1004, S1095｜gematsu.com / pocketgamer.biz｜June 17；本地证据：release_calendar 多源
- 产品日历 - 夜幕之下 —— S0760, S0882｜3839.com / new.qq.com｜https://www.3839.com/a/182365.htm ｜本地证据：release_calendar + industry_news（厂商/品类回填）双来源
- 产品日历 - 料理人班乔 —— S0875, S1065｜youxichaguan.com / gamelook.com.cn｜https://youxichaguan.com/archives/197674 ｜厂商/IP 回填自 industry_news
- 产品日历 - 影之刃零 —— S0874, S0767｜youxichaguan.com / gematsu.com｜https://youxichaguan.com/archives/197660 ｜本地证据：release_calendar + industry_news 双覆盖（延期事件）

### 四、玩家舆论 / 社区动态

1. 《鸣潮》2077联动卡池被爆独立保底+副产物缩水，玩家质疑变相涨价 —— S0289, S0296, S0829, S1009｜bbs.nga.cn｜https://bbs.nga.cn/read.php?tid=46882152
2. 《燕云十六声》新地图NPC"付鹏举""忮忌"被指阴阳岳飞，三轮改动仍未平息 —— S0360, S0364, S0419, S0828, S0833, S1018｜bbs.nga.cn｜https://bbs.nga.cn/read.php?tid=46886352
3. 《重返未来：1999》三周年PV被冲240万条评论，制作组发长文致歉 —— S0298, S0441, S0366｜bbs.nga.cn / gamelook.com.cn｜http://www.gamelook.com.cn/2026/06/594392/
4. 《洛克王国 世界》女角色"鸭子坐"动作差分引发性别争议，官方删改反复 —— S0293, S0415, S0163, S0294, S0408, S0417｜bbs.nga.cn｜https://bbs.nga.cn/read.php?tid=46857960（女洛鸭子坐核心：S0293；男洛露出支线：S0415；宝可梦视频被举报：S0163；收场/流水：S0294/S0417）

### 五、行业精选 / 深度观察

1. 微信小游戏5亿MAU：真正的增量已经在PC端 —— S0006, S0003, S0044｜gamelook.com.cn / new.qq.com｜http://www.gamelook.com.cn/2026/05/594154/
2. 国产搜打撤集中立项，赛道向硬核与轻量化两端分化 —— S0676, S0208, S0657, S0001｜new.qq.com / gamelook.com.cn / gcores.com｜http://www.gamelook.com.cn/2026/05/594255/

## release_calendar 本地证据信号汇总

- 强（calendar + industry_news 同游戏重合）：鸣潮、夜幕之下、影之刃零。
- 强（跨多个 calendar 源）：崩坏：星穹铁道（3839+17173）、宝可梦 Champions（gematsu+pocketgamer/3839）。

## 被排除的值得注意条目（与理由）

- 海外主机/3A/硬件弱相关：Steam Deck OLED 涨价（S0050/S0084）、巫师3/巫师4（S0229/S0467）、Fable 延期（S0464）、007/MGM/Amazon 发行权（S1090）、Balatro/Playstack 出售（S0244/S0641）、铁拳8 总监离职（S0669）、Rockstar 工会/PlayerUnknown 裁员/Team17 裁员（S0469/S1088/S1102）、PlayStation 一方销量/State of Play/Switch 2 销量/ROG Xbox Ally/CoD 退主机（S0681/S0917/S1117/S0489/S0248）。理由：对用户业务（移动/竞技/生活模拟/数值卡牌/跨平台）无 1 个以上具体迁移点。
- 远期常规定档（非当下、相关性不足）：沙丘：觉醒（S0766，9/22 主机开放世界生存）、寂静岭：Townfall（S0762/S0858，9/24 主机心理恐怖）。按"远期主机定档公告不入日报/周报"规则排除（保留延期/跳票等生命周期变动如影之刃零）。
- 例行许可：中国 5 月过审 158 款版号（S0495）。按规则排除。
- 区域监管不涉 mobile/全球分发：加州 AB1921 游戏保护法案（S0672/S0889）。
- 未核到原文/单源谨慎不入：Liftoff IPO（S1102 记录为 Team17，Liftoff 实际记录另在 mobilegamer，本轮未核）、库洛投资前崩铁技术负责人、网易撤资 Quantic Dream（S1074 单源）。
- IP/动画整合、游戏侧在研、迁移弱：阅文 4 亿收购艺画开天（S0881）。
- Hard Stop 2 强制排除（仅审计留痕，正文绝不出现）：沐瞳 / Mobile Legends: Bang Bang / 决胜巅峰相关——S0501（决胜巅峰电竞世俱杯）、S0879（决胜巅峰土耳其联赛）、S0676 原文内提及的"头号禁区"。

## 缺失数据说明

- `deep_analysis` 缺 2026-05-31 一天；其余 section 5/28–6/4 齐全。
- pc_rankings：原 2026-06-04 SteamDB 采集失败，本轮改用 Steam 官方周榜重新采集，最近完整周为 of 2026-05-26，已在正文注明。
