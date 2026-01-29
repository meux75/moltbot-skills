# AI Coding Agent Instructions for Clawd Workspace

## Project Overview

This is a **Philippine Stock Exchange (PSE) trading research and data analysis platform** combined with an **AI agent framework** (Clawdbot-based). The workspace serves dual purposes:

1. **Trading System**: Automated PSE stock data collection, fundamental/technical screening, and position research
2. **Agent Framework**: Infrastructure for autonomous AI agents to maintain continuity, memory, and task execution

## Critical Session Setup (READ FIRST)

Before any task, **always** in this order:
1. Read `SOUL.md` — Agent identity and operating principles
2. Read `USER.md` — Human context and constraints  
3. Read `memory/YYYY-MM-DD.md` (today + yesterday) — Recent decisions and state
4. If in main session: Read `MEMORY.md` — Long-term curated memory

This prevents repeated work, respects privacy, and aligns with user intent. No exceptions.

## Architecture & Data Flow

### PSE Data Collection Pipeline

**Two parallel collectors** in root:
- [brave_pse_collector.py](brave_pse_collector.py) — Brave API integration (preferred, real data)
- [pse_data_collector.py](pse_data_collector.py) — Fallback web scraper (Investing.com)

Both output to `pse_data/` CSV files with schema:
```
symbol | timestamp | current_price | change | volume | vwap | technical_signal
```

**Stock screening workflow:**
1. Collectors fetch live PSE quotes
2. [PSE_Stock_Screening_Framework.md](PSE_Stock_Screening_Framework.md) defines 6 screening categories
3. [skills/yahoo-finance/yf](skills/yahoo-finance/yf) — Pulls fundamentals (PE, EPS, margins, ROE) for deeper analysis
4. Analysis exported to `pse_data/brave_analysis_summary.txt`

### Agent Memory Architecture

Memory is layered (read `AGENTS.md` for full spec):

| Type | File | Purpose | Load When |
|------|------|---------|-----------|
| **Daily** | `memory/YYYY-MM-DD.md` | Raw logs, decisions, context | Every session |
| **Long-term** | `MEMORY.md` | Curated memories, lessons | Main session only |
| **Skills** | `skills/*/SKILL.md` | Tool documentation | On-demand |
| **Identity** | `SOUL.md`, `IDENTITY.md` | Who the agent is, values | Every session |

**Critical rule**: Never leak `MEMORY.md` to group chats or shared contexts — contains personal data.

## Development Workflows

### Running Stock Analysis

```bash
# Collect current PSE data
python3 brave_pse_collector.py

# Get fundamentals for specific stock  
./skills/yahoo-finance/yf fundamentals BDO
./skills/yahoo-finance/yf quote JFC

# Analysis outputs to
cat pse_data/brave_analysis_summary.txt
```

**Dependencies**: Python 3.11+, `requests`, `yfinance`. The `yf` script auto-installs via `uv` (PEP 723).

### Logging & Debugging

- `pse_data_collector.log` — Main collector logs
- All scripts use `logging.INFO` level
- Check logs first when data fetch fails

### Memory Updates (Non-Negotiable)

When you **complete meaningful work**:
- **Update `memory/YYYY-MM-DD.md`** with what was done, why, outcomes
- **Update `AGENTS.md`** if you discover new workflows or lessons
- **Update `MEMORY.md`** (main session only) if it affects future strategy
- **Never make mental notes** — text files are the source of truth

Example:
```markdown
# Daily Log - 2026-01-29

## PSE Screening Completed
- Analyzed 23 mid-cap stocks using technical + fundamental filters
- BDO emerging as strong position: P/E 10.2x, ROE 15.3%, MACD positive
- Filtering notes saved to analysis_summary.txt
- Recommend deeper due diligence on BDO, SM, JFC
```

## Code Patterns & Conventions

### Python Scripts (Data Collection)

All collectors follow this pattern:
```python
class Collector:
    def __init__(self):
        self.data_dir = "pse_data"
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """Create pse_data/ if missing"""
        
    def fetch_data(self, symbol):
        """Return dict: {'symbol', 'current_price', 'timestamp', 'success', 'error'}"""
        
    def save_to_csv(self, data_list):
        """Write to pse_data/{timestamp}_analysis.csv"""
```

**Key conventions:**
- Use `logging.basicConfig()` at module level
- All external calls have try/except + logging
- Output always goes to `pse_data/` (checked into git)
- Timestamps use ISO format: `datetime.now().isoformat()`

### Skills Structure

Skills live in `skills/{skill-name}/` and contain:
- `SKILL.md` — Documentation (commands, requirements, examples)
- Executable script or directory with code
- Example: `skills/yahoo-finance/yf` is a Python CLI

**To invoke skill:**
```bash
./skills/yahoo-finance/yf quote SYMBOL
./skills/yahoo-finance/yf fundamentals SYMBOL
```

Skills are agent-independent utilities — should work standalone.

## Group Chat & Integration Rules

The workspace integrates with Telegram (`TELEGRAM.md` has token details).

**When contributing to group chats:**
- Respond only when directly mentioned or adding genuine value
- Don't respond to every message (humans don't either)
- Use emoji reactions naturally instead of text replies
- Never paste sensitive data (tokens, prices beyond what's needed)
- In trading discussions, cite your sources (e.g., "Per PSE data collected 2026-01-28")

Read `AGENTS.md` "Group Chats" section for full philosophy.

## Security & Safety

**Do freely:**
- Read any file in workspace
- Run collectors and analysis scripts
- Update memory files
- Search web for stock data

**Ask first:**
- Posting trade signals publicly
- Sending emails/tweets
- Modifying user's calendar or contacts
- Anything leaving the machine that's not explicitly part of workflow

**Never:**
- Exfiltrate `MEMORY.md` outside main session
- Run destructive commands (`rm`, `git reset`) without confirmation
- Share position recommendations as financial advice
- Commit credentials to git (check `.gitignore`)

## File Structure Quick Reference

```
clawd/
├── AGENTS.md                    # Agent framework docs (READ FIRST)
├── SOUL.md                      # Agent identity & principles
├── MEMORY.md                    # Long-term curated memory (main session only)
├── memory/YYYY-MM-DD.md         # Daily logs (READ EVERY SESSION)
├── IDENTITY.md                  # Extended agent profile
├── USER.md                      # Human context & preferences
├── PSE_Stock_Screening_Framework.md  # Stock filtering criteria
├── TOOLS.md                     # Environment-specific notes
├── TELEGRAM.md                  # Bot integration details
├── pse_data_collector.py        # Data collector (web scraper)
├── brave_pse_collector.py       # Data collector (Brave API)
├── pse_data/                    # CSV outputs & analysis summaries
└── skills/yahoo-finance/
    ├── SKILL.md                 # yfinance CLI documentation
    └── yf                       # Executable (get quotes, fundamentals)
```

## Common Tasks

### "Analyze stock X"
1. Check `PSE_Stock_Screening_Framework.md` for applicable criteria
2. Run: `./skills/yahoo-finance/yf quote X && ./skills/yahoo-finance/yf fundamentals X`
3. Compare metrics (PE, ROE, margins) against framework thresholds
4. Document findings in memory

### "Update stock screening data"
1. Run: `python3 brave_pse_collector.py`
2. Check `pse_data_collector.log` for errors
3. Review generated analysis in `pse_data/brave_analysis_summary.txt`
4. Update `memory/YYYY-MM-DD.md` with what was found

### "What happened yesterday?"
1. Read `memory/YYYY-MM-DD.md` (yesterday's date)
2. Skim recent entries in `MEMORY.md`
3. Check git log if code changed

### "Add new stock to screening"
1. Verify it exists on PSE (check screening framework for universe)
2. Update both collector scripts to include new symbol
3. Run collectors to validate API/scraper works
4. Document in memory why this stock is relevant

## Iteration & Feedback

This file is a living guide. When you discover:
- **Missing patterns** → Add them here with examples
- **Workflow improvements** → Document the better way
- **Common mistakes** → Call them out (e.g., "Don't assume MEMORY.md is loaded")
- **Outdated instructions** → Fix them immediately

Tell the user what changed — this is working knowledge, not just reference.
