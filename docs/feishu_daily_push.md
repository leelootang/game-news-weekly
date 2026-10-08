# Feishu Daily Report Push

## 周四深度观察备选 Bot

周四备选使用独立飞书应用，不复用日报订阅 Bot。`FeishuDeepReviewListener` 在用户登录后保持长连接，首次私聊会把该应用专属 `open_id` 绑定到本地；之后周四任务将目标周报的全部合格候选分批发送到该私聊。

回复必须同时包含正文与卡片，例如 `正文：C005，C001；卡片：C005`。需要融合时可写 `卡片：把 C005、C006、C014 的信息整合成 Wardogs 成绩复盘；正文：C005，C001`，其中卡片第一个编号是主卡并且必须进入正文，后续编号仅作为整合参考。最新一条有效回复覆盖此前回复。

每条有效回复立即写入 `data/feishu/deep_review/replies/`（该目录不入库）。周五 09:00 任务先读取目标周报 ID 对应的最新回执，再生成 `output/deep_observation_review/<目标周报ID>_selection.md`。selection 必须写选择来源、回执 ID、正文候选 ID、指定卡片候选 ID及可选的卡片整合参考 ID，并通过 `deep_observation_handoff.py lint-selection`。没有有效回复时，周报继续生成但省略深度观察，不自动代选；存在有效回复但整理或校验失败时交给 09:40 兜底任务重试，不能静默忽略。

凭据保存在已被 Git 忽略的 `.env.local`，变量名为 `FEISHU_DEEP_REVIEW_APP_ID` 与 `FEISHU_DEEP_REVIEW_APP_SECRET`。本地电脑需保持开机、用户已登录且监听任务运行；换电脑或新应用首次使用时需重新私聊绑定。

This project supports a private-message subscription flow for the daily game
industry report:

```text
User sends "订阅日报" to the bot
Feishu sends im.message.receive_v1 to this service
The service stores the user's open_id
The daily publisher sends a report card to active subscribers
```

## Environment

Keep secrets in `.env.local`:

```env
FEISHU_APP_ID=cli_xxx
FEISHU_APP_SECRET=xxx
FEISHU_DAILY_FOLDER_TOKEN=xxx
```

`FEISHU_APP_ID` and `FEISHU_APP_SECRET` are required for sending messages and
creating documents. `FEISHU_DAILY_FOLDER_TOKEN` is the drive folder that daily
docx documents are imported into (see `--create-doc` below).

Check local config without printing secrets:

```powershell
python scripts/feishu_common.py
```

## Event Receiver (Long Connection)

Subscriptions are received over a Feishu long connection — no public tunnel or
callback URL is required. In the Feishu app console set the event receiving mode
to 长连接 and subscribe to:

```text
im.message.receive_v1
```

Then run the listener:

```powershell
python scripts/feishu_subscribe_listener.py
```

Note: `lark-oapi`'s top-level import is slow on Python 3.14 (~40s one-time
startup), but the WebSocket connection itself is stable. Keep the process
running so new subscriptions are captured. Supported commands:

- `订阅日报`
- `退订日报`

Subscriber data is stored locally under `data/feishu/`, which is ignored by Git.

## Publish A Daily Card

Dry-run a historical report:

```powershell
python scripts/publish_feishu_daily.py --date 2026-06-20 --dry-run
```

Send to one user for testing, creating the docx automatically:

```powershell
python scripts/publish_feishu_daily.py --date 2026-06-20 --create-doc --to-open-id ou_xxx
```

Send to all active subscribers:

```powershell
python scripts/publish_feishu_daily.py --date 2026-06-20 --create-doc
```

The report card uses a shared default limit of 10 items per section across
broadcast, backfill, menu replay, and feedback expansion. Player discourse has
a stricter cap: 2 items for daily/weekend reports and 3 for weekly reports.
AI news uses the same compact information density as industry news: headline
plus one factual extension on the same line. Industry decisions marked
`card_carryover=true` are guaranteed one of those ten positions but render
exactly like ordinary industry items. Carryover is internal selection metadata
and must not appear in the card or Feishu document. The publish log records the exact rendered
`card_items`, the limit, audience scope, and whether a majority of the
subscriber broadcast succeeded.  Only that successful subscriber broadcast
counts as global card exposure; dry-runs and single-user tests do not.

`--create-doc` imports `output/daily/<date>/game_industry_daily_<date>.md` into a
Feishu docx (in `FEISHU_DAILY_FOLDER_TOKEN`, overridable with `--folder-token`),
sets it to organization link-readable, and attaches its URL to the card. The
target folder must have the bot app added as an editor, and the app needs the
`docs:document:import` (or `drive:drive`) scope. Without `--create-doc` you can
still pass a fixed URL via `--doc-url` or the `FEISHU_DAILY_DOC_URL_TEMPLATE`
environment variable.
