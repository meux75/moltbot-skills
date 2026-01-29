# Forex Fundamental Analysis Skill

A comprehensive skill for Forex fundamental analysis based on professional trading strategies. This skill provides tools for economic data analysis, market sentiment tracking, and systematic fundamental trading.

## Core Components

### 📊 Market Session Analysis
- **24/5 Forex Market**: New York, Tokyo, Sydney, London sessions
- **Session Overlaps**: Identify optimal trading times (8-11am EST: London/New York, 19-1am EST: Sydney/Tokyo)
- **Liquidity Analysis**: Track market participation levels

### 🏦 Central Bank Focus
- **Mandate Tracking**: Price stability (primary), Employment (US Federal Reserve dual mandate)
- **Policy Tools**: Interest rates, quantitative easing, price limits, forward guidance
- **Language Analysis**: Central bank statements and policy signals

### 📈 Economic Indicators
- **High Impact**: NFP, CPI, Interest Rate Decisions
- **Medium Impact**: Retail Sales, GDP, PMI
- **Low Impact**: Balance of Trade, other secondary indicators

### 🔗 Fundamental Correlations
- **PPI → CPI**: Producer price index predicts consumer inflation
- **Retail Sales → GDP**: Monthly retail data predicts quarterly GDP
- **Housing → Durable Goods**: Home sales predict appliance purchases
- **PMI → GDP**: Manufacturing index predicts economic growth
- **ADP → NFP**: Private sector employment predicts non-farm payrolls
- **Jobless Claims → Unemployment**: Weekly claims predict monthly unemployment

### 📰 News Sources Integration
- **Primary**: Bloomberg, FXStreet, ForexFactory
- **Premium**: RanSquid, Lorettatrade ($25/month)
- **Economic Calendars**: Automated tracking of upcoming releases

## Features

### 1. Market Overview Module
```bash
# Get current market sentiment and overview
forex-fundamentals market-overview

# Analyze recent price moves
forex-fundamentals analyze-moves

# Session overlap analysis
forex-fundamentals session-analysis
```

### 2. Economic Calendar Integration
```bash
# Today's economic events
forex-fundamentals calendar today

# This week's events
forex-fundamentals calendar week

# High-impact events only
forex-fundamentals calendar high-impact

# Custom country/indicator filtering
forex-fundamentals calendar --country US --indicator CPI,NFP
```

### 3. Fundamental Analysis Tools
```bash
# Currency fundamental outlook
forex-fundamentals outlook USD

# Central bank policy focus
forex-fundamentals central-bank focus EUR

# Economic correlation analysis
forex-fundamentals correlate PPI CPI

# Market sentiment analysis
forex-fundamentals sentiment
```

### 4. Trading Signal Generation
```bash
# Generate trade opportunities
forex-fundamentals signals

# News-based entry opportunities
forex-fundamentals news-signals

# Correlation-based predictions
forex-fundamentals predict CPI --using PPI-data
```

### 5. Data Collection & Storage
```bash
# Collect economic data
forex-fundamentals collect CPI

# Store historical data
forex-fundamentals archive --indicator NFP

# Backtest strategies
forex-fundamentals backtest --period 3mo
```

## Configuration

### Environment Setup
```bash
# Install dependencies
pip install pandas numpy requests beautifulsoup4 schedule

# Configure data sources
forex-fundamentals config --set api-key YOUR_API_KEY
forex-fundamentals config --set news-source fxstreet
```

### Data Sources Configuration
```json
{
  "economic_calendar": {
    "fxstreet": {
      "url": "https://www.fxstreet.com/economic-calendar",
      "enabled": true
    },
    "forexfactory": {
      "url": "https://www.forexfactory.com/calendar.php",
      "enabled": true
    }
  },
  "news_sources": {
    "bloomberg": {
      "url": "https://www.bloomberg.com/markets/currencies",
      "enabled": true
    },
    "lorettatrade": {
      "url": "https://www.lorettatrade.com/news-feed",
      "enabled": false,
      "cost": 25
    }
  }
}
```

## Usage Examples

### Daily Trading Routine
```bash
# Morning routine - Market overview
forex-fundamentals market-overview

# Check economic calendar
forex-fundamentals calendar today

# Analyze currency fundamentals
forex-fundamentals outlook GBP

# Generate trading signals
forex-fundamentals signals
```

### Event-Specific Analysis
```bash
# Before NFP release
forex-fundamentals predict NFP --using ADP-data --using PMI-data
forex-fundamentals correlate ADP NFP

# Post-NFP analysis
forex-fundamentals analyze-moves --after NFP
forex-fundamentals sentiment --post-announcement
```

### Correlation Analysis
```bash
# PPI-CPI correlation
forex-fundamentals correlate PPI CPI --historical 6mo

# Retail Sales-GDP correlation
forex-fundamentals correlate RetailSales GDP --quarterly

# Housing-Durable goods correlation
forex-fundamentals correlate Housing DurableGoods --monthly
```

## Data Models

### Economic Event Structure
```python
{
  "id": "unique_event_id",
  "country": "US",
  "currency": "USD",
  "indicator": "NFP",
  "name": "Non-Farm Payrolls",
  "time": "2024-01-05 13:30:00",
  "impact": "high",
  "previous": "216K",
  "forecast": "200K",
  "actual": "223K",
  "deviation": "+23K",
  "market_response": {
    "pip_move": 150,
    "duration": "2h",
    "sentiment": "bullish"
  }
}
```

### Currency Fundamental Outlook
```python
{
  "currency": "USD",
  "outlook": "bullish",
  "strength": "strong",
  "central_bank_focus": ["inflation", "employment"],
  "policy_direction": "hawkish",
  "key_factors": [
    "high inflation expectations",
    "strong employment data",
    "quantitative tightening"
  ],
  "risk_factors": [
    "geopolitical tensions",
    "economic slowdown fears"
  ]
}
```

### Trading Signal Structure
```python
{
  "signal_id": "signal_12345",
  "currency_pair": "EURUSD",
  "direction": "sell",
  "confidence": "high",
  "reason": "NFP data better than expected aligns with USD bullish outlook",
  "entry_price": 1.0850,
  "stop_loss": 1.0900,
  "take_profit": 1.0800,
  "risk_reward_ratio": "1:2",
  "timeframe": "4h",
  "fundamental_basis": {
    "news_event": "NFP",
    "market_sentiment": "risk_on",
    "correlation_support": "ADP positive"
  },
  "timestamp": "2024-01-05 14:00:00"
}
```

## Advanced Features

### 1. Automated News Monitoring
- Real-time news feed parsing
- Sentiment analysis for news events
- Automated signal generation based on news

### 2. Economic Data Correlation Engine
- Cross-indicator correlation tracking
- Predictive modeling using leading indicators
- Historical correlation database

### 3. Market Sentiment Analysis
- Real-time sentiment tracking
- Risk-on/risk-off measurement
- Institutional order flow analysis

### 4. Backtesting Framework
- Historical fundamental data simulation
- Strategy performance analysis
- Optimization parameters

### 5. Risk Management Tools
- Position sizing based on fundamental strength
- Stop-loss optimization
- Correlation-based risk assessment

## Implementation Strategy

### Phase 1: Core Framework
- Basic economic calendar integration
- Market session analysis
- Simple fundamental data collection

### Phase 2: Advanced Analysis
- Correlation analysis engine
- Sentiment tracking
- Signal generation

### Phase 3: Professional Features
- Automated monitoring
- Backtesting capabilities
- Risk management tools

## Requirements

- Python 3.8+
- pandas, numpy, requests
- BeautifulSoup4 for web scraping
- Schedule for automated updates
- Optional: News API integration

This skill provides a comprehensive framework for systematic Forex fundamental analysis based on professional trading methodologies.