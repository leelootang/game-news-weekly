# 重建完成与校验回执

- 锚点：星期四，日报，date=2026-10-14，Asia/Shanghai。
- 本次重建：2026-10-15 10:56:44—11:33:08 +08:00，约37分钟。
- 输入：236条，抽取失败0，空正文0；最终引用39条，全部body_status=full。
- 输出计数：行业17 / AI8 / 产品日历1 / 社区2 / 深度1。
- 行业历史：2026-09-30至2026-10-13，共71次记录；5类已曝光重复事件排除，无material_update，无card_carryover。
- 校验命令一：report_lint.py显式传canonical --report、--sources、--inputs、--report-type daily，退出0，0 error。
- 校验命令二：report_artifacts.py validate显式传canonical报告、来源、输入、items、decisions、release-audit及--require-artifacts，退出0，0 error。
- 剩余warning：38条非全文输入未用于终稿；AI8超1–3软目标，5条直接应用+3条有明确迁移链的新能力，采用理由见selection_decisions.md。
- 采集覆盖缺口：4源failed（dataeye_36kr、nadianshi、cubox、wanjiang_16p_newgame）；2源degraded（pocketgamer、vgc）。这不是本轮抽取报错，不联网补造。
- 最终正文禁词/内部标记扫描：0命中。
- news_data的git diff为空；未修改采集源数据、脚本或skill，未git add/commit/push。
- 早版备份：本目录下superseded_morning_20261015_rebuild。没有删除早版；可从备份恢复。
- 本次只更新Markdown、自动生成的sources_used与中间产物；未操作飞书、Docs、网页。已有早版网页/文档不代表本次新版。
- Canonical Markdown SHA256：58EC296991A0414C62F427906C11FED3739433B52A8FFE1C35B5C248497311E8。
