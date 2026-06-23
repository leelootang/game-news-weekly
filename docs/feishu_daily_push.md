# Feishu Daily Report Push

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

`--create-doc` imports `output/daily/<date>/game_industry_daily_<date>.md` into a
Feishu docx (in `FEISHU_DAILY_FOLDER_TOKEN`, overridable with `--folder-token`),
sets it to organization link-readable, and attaches its URL to the card. The
target folder must have the bot app added as an editor, and the app needs the
`docs:document:import` (or `drive:drive`) scope. Without `--create-doc` you can
still pass a fixed URL via `--doc-url` or the `FEISHU_DAILY_DOC_URL_TEMPLATE`
environment variable.
