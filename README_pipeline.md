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

The Steam ranking section (`pc_rankings`) has been retired from daily/weekly/
monthly reports; it is no longer extracted, rendered, or collected. To run the
extractor explicitly, pass the active sections:

```powershell
python <skill_root>\scripts\extract_report_inputs.py --workspace . --date 2026-06-04 --report-type daily --sections industry_news ai_trends release_calendar community_discourse deep_analysis
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
- `deep_analysis`: newsletters, essays, and long-form industry analysis
- `community_discourse`: player opinion, community incidents, and forum/social excerpts

The `pc_rankings` section (PC bestseller / SteamDB snapshots) is retired and no
longer part of report generation; the `steamdb_rankings` collector remains in the
tree but is dormant (not invoked by the scheduled runner).

The runner still accepts legacy aliases: `market_news`, `ai_news`,
`product_launches`, `newsletter`, and `player_discourse`.

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

## Report Scoring Policy

Industry scoring uses `subject_genre_v2`: E remains event type (0–3), R is subject importance (0–3), and M is binary priority-genre bonus (0/1). All report types require E×R+M ≥5; E0 is excluded. There is no industry count cap. Source quality, report dates and exposure-aware deduplication remain independent gates.

`config/game_report_policy.json` and `scripts/report_policy.py` are synchronized with the installed game-industry-report skill. The 35 canonical focus-subject groups are references for industry influence; unlisted subjects with comparable influence can also receive R3/R2. The canonical list still determines release-calendar company bonuses. Calendar scoring remains event×source+company with direct +3/investment +2, independent multi-source eligibility and existing caps.

New decisions use a root `scoring_version` and non-E0 industry decisions record `subject_assessment` and `genre_assessment` with verbatim source evidence. Report windows ending on/after 2026-10-21 require v2; earlier existing reports without a version retain their historical scoring. Rebuilt reports explicitly use v2. The calendar sync preserves root metadata. Both lint and artifact validation enforce the new policy. Card maximum-score emphasis is 10 for v2 and 11 for legacy reports.

Run policy, calendar, artifact, lint integration and card tests after policy changes. Skill mirrors must remain identical; archived reports and their generation scripts are historical artifacts, not live policy definitions.

The versioned skill, including the extractor, lint, references and policy copies,
is included at `skills/game-industry-report/`. Integration tests use this bundled
copy so a checkout does not depend on one user's absolute installation path.
When updating the installed skill, synchronize this directory and the shared
workspace modules/config in the same change. Existing automations can continue
using their installed skill path; this checkout does not change that installation.

Run the relevant offline regressions without installing pytest:

```powershell
$env:PYTHONUTF8 = "1"
python scripts/run_report_regressions.py --output-dir output/validation/report-regressions
```

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
- If only a source-provided excerpt is available, set `fetch_status: partial` and
  `fallback: source_excerpt`; do not present it as a fully extracted article.

## Newly Registered Sources (2026-07-15)

The following collectors were audited before registration. They use source RSS,
official APIs/sitemaps, or server-rendered source pages; none relies on screenshots
or generated summaries. All write through the existing `article_store.py` contract
and inherit the runner's section/date output path and manifest handling.

| Collector | Report section | Discovery / body method | Notes |
| --- | --- | --- | --- |
| `baoyu` | `ai_trends` | RSS + article page | Full post body from the source prose block. |
| `chuapp` | `industry_news` | Full-text RSS | Source body is in RSS description. |
| `gameoracle` | `deep_analysis` | Sitemap + JSON-LD/article page | Long-form Steam market analysis. |
| `gameres` | `industry_news` | Homepage + article page | Limits discovery to GameRes original articles. |
| `gamespot` | `industry_news` | Publisher RSS | Structured, untruncated article bodies can be full; short or truncated entries remain partial. |
| `ign_cn` | `industry_news` | RSS + article-page fallback | Short RSS teasers are replaced with the server-rendered article body. |
| `indienova` | `industry_news` | News index + article page | Handles absolute and relative Chinese dates. |
| `luosiji_sohu` | `industry_news` | Official Sohu account API + article page | Uses excerpt only when the page body cannot be read, and marks it. |
| `matthewball` | `deep_analysis` | Full-text RSS | Long-form strategy and media-economics essays. |
| `nadianshi` | `industry_news` | 今日关注 category + article page | Full-text Chinese mobile-game industry reporting. |
| `necromanov` | `deep_analysis` | Full-text WordPress RSS | Low-frequency game analysis. |
| `pcgamer` | `industry_news` | Full-text RSS | High-volume source; editorial filtering happens downstream. |
| `polygon` | `industry_news` | Full-text RSS | Games and adjacent entertainment coverage. |
| `qimai_sohu` | `industry_news` | Official Sohu account API + article page | Uses excerpt only when the page body cannot be read, and marks it. |
| `questmobile` | `deep_analysis` | Official report-list API | The source supplies report introductions, stored explicitly as `partial`. |
| `roblox_newsroom` | `industry_news` | Server-rendered catalog + article page | Official Roblox announcements with full article text and metadata. |
| `sensortower` | `deep_analysis` | Chinese-blog sitemap + article page | Market intelligence reports. |
| `unrealengine` | `ai_trends` | Full-text RSS | Official engine, tooling, and developer-tech signals. |
| `yxrb` | `industry_news` | Mobile index + article page | Deduplicates repeated mobile-list titles within a run. |

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
- `chuapp`
- `gameres`
- `gamespot`
- `ign_cn`
- `indienova`
- `luosiji_sohu`
- `pcgamer`
- `polygon`
- `qimai_sohu`
- `yxrb`
- `roblox_newsroom`
- `nadianshi`
- `aihot`
- `baoyu`
- `unrealengine`
- `gamediscover`
- `naavik_digest`
- `thegamebusiness`
- `deconstructor_deconstructions`
- `gameoracle`
- `matthewball`
- `necromanov`
- `questmobile`
- `sensortower`
- `ceshibiao_17173`
- `wanjiang_16p_newgame`
- `haoyou_kuaibao_3839`
- `taptap_app_calendar`
- `gematsu_release_dates`
- `nga_mobile_gossip`
- `reddit_gaming_rising`

`steamdb_rankings` still exists in the tree but is dormant — the Steam ranking
section is retired, so the scheduled runner no longer invokes it.

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

PocketGamer uses a separate persistent browser profile at
`data/browser_sessions/pocketgamer/`, which is excluded from Git. Its default
browser channel is installed Chrome; `--browser-channel chromium` selects the
Playwright-managed browser instead. The setup helper
`scripts/setup_pocketgamer_browser.cmd` allows the user to complete website
verification in that dedicated browser. Verification can expire, and an accepted
session does not guarantee unattended detail retrieval: blocked details remain
explicit RSS-summary fallbacks, while an existing full article is retained.

## 行业新闻时间口径

自2026-10-27采用 source_window_v1：行业窗口按本期来源 published_at（缺失回退抽取 date）召回，事件发生日期不设准入门槛。当期报道的未收录未曝光旧事件，只要 E×R+M≥5 且取证合格就可入选，不要求当期首次披露。正文保留真实历史语态。双周历史与更早 archive_occurrences 共同核对曝光，已曝光的同事件没有实质更新仍排除；曾入正文但未上卡片的原有至多1条规则不变。产品日历等分区仍执行各自日期规则。

selection_decisions.json 写 industry_timing_version；非E0行业候选写 time_check，exclude 写具体 exclusion_gates，不能只写事件超窗。scripts/industry_timing.py 为日期审计与两道 lint 的共用实现；安装技能含相同副本。sync_release_decisions.py 保留时间与评分版本。

行业R以名单为影响力参照，开放同等影响力的名单外主体：`comparable_major_subject`对应R3，`comparable_significant_subject`对应R2；用现有basis/evidence说明产品覆盖、规模或行业地位等综合判断，不设新硬性数值线。未列名不构成R1上限；产品日历名单公司加分仍独立。
