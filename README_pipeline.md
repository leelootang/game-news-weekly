# AI Game Industry News Pipeline

This workspace collects game-industry inputs for daily, weekly, and monthly
reports. The pipeline now stores article bodies as structured text by default,
with PDFs kept only as an explicit fallback path.

## Output Model

Daily collectors are still orchestrated by `run_daily_collectors.py`, and the
runner still owns section/date folders and centralized run manifests.

Default article body output:

```text
news_data/<section>/YYYY-MM-DD/articles.jsonl
news_data/<section>/YYYY-MM-DD/articles_index.md
```

Run metadata and collector manifests:

```text
news_data/_collector_runs/YYYY-MM-DD/
```

PDF output is disabled by default. To render PDFs for a debugging or emergency
fallback run, set:

```powershell
$env:NEWS_SAVE_PDF = "1"
```

When PDF saving is enabled, collectors write article PDFs under:

```text
news_data/<section>/YYYY-MM-DD/
```

## Article Records

Each line in `articles.jsonl` is one collected item. Records include:

- `title`
- `url`: original source URL
- `source` and `source_key`
- `published_at`
- `text`: extracted readable body or structured event/forum text
- `html`: cleaned source HTML when available
- `excerpt`: source-provided excerpt when available
- `fetch_status`
- `fallback`: `none` by default; examples include `source_excerpt`
- `extra`: source-specific fields such as author, tags, score, rank, comments,
  event metadata, or raw publish timestamps

`summary` is not an AI-generated field in the collection step. If a source
provides an RSS/list excerpt, it is stored as `excerpt` or source-specific
metadata. AI summarization belongs to the report-writing stage, not the crawler.

`articles_index.md` is regenerated beside each JSONL file whenever a collector
writes an article. It is the quick human QA view: title, source, publish time,
fetch status, body length, and source link in one table. To rebuild indexes for
existing data, run:

```powershell
python scripts/build_article_indexes.py
```

## Report Extraction

The report input extractor reads structured text first:

```text
news_data/<section>/YYYY-MM-DD/articles.jsonl
```

When SteamDB rankings should appear in a report, include the ranking section in
the extractor call:

```powershell
python <skill_root>\scripts\extract_report_inputs.py --workspace . --date 2026-06-04 --report-type daily --sections industry_news ai_trends release_calendar pc_rankings community_discourse deep_analysis
```

It also reads old PDFs from:

```text
news_data/<section>/YYYY-MM-DD/*.pdf
news_pdfs/<section>/YYYY-MM-DD/
```

This lets new text-based runs and historical PDF-based runs coexist during the
migration. `news_pdfs` is legacy-only and should not receive new output.
Duplicate URLs/titles in the same section/date are skipped so JSONL records take
priority over older PDFs.

For report QA, build a readable title index next to every
`_intermediate/report_inputs.jsonl`:

```powershell
python scripts/build_report_input_indexes.py
```

This creates `_intermediate/report_inputs_index.md`, grouped by report section
with source IDs, titles, sources, body lengths, statuses, and links. Use it
before judging whether the AI selected or missed important stories.

## Report Sections

Collectors are registered under section keys:

- `industry_news`: market, company, platform, and industry news
- `ai_trends`: AI-specific news and tooling signals relevant to games
- `release_calendar`: game launch, beta, update, and product-event tracking
- `pc_rankings`: PC bestseller rankings and SteamDB market-signal snapshots
- `deep_analysis`: newsletters, essays, and long-form industry analysis
- `community_discourse`: player opinion, community incidents, and forum/social excerpts

The runner still accepts legacy aliases: `market_news`, `ai_news`,
`product_launches`, `newsletter`, and `player_discourse`. It also accepts
`rankings` as an alias for `pc_rankings`.

## Daily Collection

Run all collectors for yesterday:

```powershell
python run_daily_collectors.py --preset yesterday
```

Run a pinned day:

```powershell
python run_daily_collectors.py --since 2026-05-26 --until 2026-05-27
```

Run one collector:

```powershell
python run_daily_collectors.py --collectors aihot --since 2026-05-26 --until 2026-05-27
```

Debug one article:

```powershell
python run_daily_collectors.py --collectors gcores --preset today --limit 1 --max-pages 1
```

Useful progress options:

```powershell
python run_daily_collectors.py --preset yesterday --no-progress
python run_daily_collectors.py --preset yesterday --show-collector-output
```

After each run, inspect:

```text
news_data/_collector_runs/YYYY-MM-DD/run_summary.md
news_data/<section>/YYYY-MM-DD/articles_index.md
```

The summary reports collector status, health, in-window item counts, and titles.

## Log Retention & Storage

The runner calls `prune_old_logs()` at the start of every run:

- `news_data/_collector_runs/YYYY-MM-DD/` folders older than **90 days** are deleted (manifests + `run_summary.{md,json}`). 90 days covers a full quarterly look-back; if you need older windows preserved, copy them out manually.
- `collector_logs/daily_collectors_*.json` files older than **30 days** are deleted (legacy timestamped JSON logs; no longer written by current runner).
- **`collector_logs/scheduled/` is NOT pruned.** This subdirectory holds stdout from the Windows scheduled task (`scheduled_run.log`, appended on every fire). If the scheduled task runs daily for a year, this file will grow to tens of MB and need manual rotation. Either rotate it yourself periodically (e.g. monthly `Move-Item scheduled_run.log scheduled_run.log.YYYY-MM`) or change the scheduled task arg to overwrite (`>` instead of `>>`) if you only need the latest run's stdout.

Retention constants live at the top of `run_daily_collectors.py`:

```python
COLLECTOR_RUNS_RETENTION_DAYS = 90
LEGACY_LOG_RETENTION_DAYS = 30
```

## Skill / Lint Range Drift

`game-industry-report` skill's `report_lint.py` ships with section item-count ranges (e.g. daily industry 3–5) that were tuned for the original "少而精" doctrine. The current SKILL.md uses wider "宁多勿少" ranges (daily industry 3–7) so the user can filter. **As a result, lint will emit WARN on every report run.** WARN ≠ ERROR; the run still passes. Two ways to reconcile:

1. Sync `report_lint.py` ranges with SKILL's Section Targets table.
2. Treat WARN as informational and ignore (current default).

This drift is intentional for now — note it in your head when reading lint output.

## Collector Contract

Each collector should support:

- `--preset yesterday|today|last-7-days`
- `--since YYYY-MM-DD`
- `--until YYYY-MM-DD`
- `--out PATH`
- `--max-pages N`
- `--limit N`

Collector requirements:

- Collect all eligible items for the requested window, or fail loudly if
  completeness cannot be proven.
- Do not use `--limit` in scheduled production runs; it is for debugging.
- Keep original source URLs in both manifest entries and article records.
- Prefer stable APIs/RSS/static HTML over screenshots or PDF rendering.
- Store readable text in `articles.jsonl` by default.
- Use PDF only when `NEWS_SAVE_PDF=1`, or when a future collector has no stable
  way to obtain readable text and explicitly documents that fallback.
- Keep both normalized `published_at` and raw date fields in `extra` when useful.

## Collector List

- `gcores`
- `gamelook`
- `cgames`
- `youxiputao_sohu`
- `youxituoluo`
- `youxichaguan`
- `yystv`
- `youxixinzhi_qqnews`
- `gamesindustry`
- `pocketgamer`
- `gamedeveloper`
- `mobilegamer`
- `investgame`
- `vgc`
- `dataeye_36kr`
- `aihot`
- `gamediscover`
- `naavik_digest`
- `thegamebusiness`
- `deconstructor_deconstructions`
- `ceshibiao_17173`
- `wanjiang_16p_newgame`
- `haoyou_kuaibao_3839`
- `taptap_app_calendar`
- `gematsu_release_dates`
- `steamdb_rankings`
- `nga_mobile_gossip`
- `reddit_gaming_rising`

## SteamDB Rankings

`steamdb_rankings` writes one structured record to `pc_rankings` per run.
Single-day windows crawl `https://steamdb.info/stats/globaltopsellers/`, keep
the TOP10, and mark titles whose SteamDB release date falls in the current
month. If the collection date is before the 10th day of the month, the previous
month is included in that launch window.

Multi-day windows crawl `https://steamdb.info/topsellers/`, keep the TOP10, and
mark products whose Change value implies they were outside the previous week's
TOP10. Marked products are enriched from their SteamDB app chart pages with
publisher, release date, tags/genre, one preferred sales estimate, and
review/rating text.

## Adding A New Source

Create:

```text
collectors/<source_key>.py
```

Then register it in `run_daily_collectors.py` with its section:

```python
COLLECTORS = {
    "new_source": Collector(
        key="new_source",
        script=ROOT / "collectors" / "new_source.py",
        section="industry_news",
        default_max_pages=8,
    ),
}
```

New collectors should use `collectors/article_store.py` to write JSONL records.
The runner decides the section/date output folder; collectors should write only
to the `--out` path they receive.

## Environment Notes

The workspace currently uses Python 3.14 on this machine. Playwright and
Chromium are already installed for the local collector environment.
