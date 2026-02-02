# Forex Fundamental Analysis Skill

A comprehensive skill for Forex fundamental analysis based on professional trading strategies. This skill provides tools for economic data analysis, market sentiment tracking, and systematic fundamental trading.

## Core Components

### 📊 Market Session Analysis
- **24/5 Forex Market**: New York, Tokyo, Sydney, London sessions
- **Session Overlaps**: Identify optimal trading times (8-11am EST: London/New York, 19-1am EST: Sydney/Tokyo)
- **Liquidity Analysis**: Track market participation levels

### 🏦 Central Bank Focus
- **Federal Reserve (FOMC)**: Dual mandate (price stability + employment), 8 meetings/year, 2% inflation target
- **ECB (Governing Council)**: Price stability mandate, monthly meetings, <2% inflation target
- **Bank of England (MPC)**: Price stability + sustainable growth, monthly meetings, ~2% inflation target
- **Bank of Japan (MPC)**: Price stability, 1-2 meetings/month, export economy management
- **SNB (Governing Board)**: Price stability, quarterly meetings, export economy management
- **Bank of Canada (Governing Council)**: 1-3% inflation target, ~8 meetings/year
- **RBA (Board)**: Price stability + prosperity, 11 meetings/year, 2-3% inflation target
- **RBNZ (Governor)**: Price stability + exchange rate stability, 8 meetings/year

### 📈 US Economic Indicators (5 Major)
- **GDP (Gross Domestic Product)**: Total goods/services value, quarterly, lagging indicator
  - Rising GDP → economic growth → inflation risk → potential rate hikes
  - Negative correlation: rapid inflation → reduced demand → decreased GDP → rate cuts
- **Non-Farm Payrolls**: Total employment excluding farm/government, monthly
  - Headline number: 100K-250K typical job creation
  - Average work week: Full employment indicator
  - Average hourly earnings: Wage inflation predictor
  - High employment → wage inflation → rate hike pressure
- **Balance of Trade**: Exports - Imports, monthly ~$44B deficit for US
  - Decreasing deficit = positive for USD (less money leaving economy)
  - Increasing deficit = negative for USD (more money leaving economy)
- **TICS (Treasury International Capital Survey)**: Foreign investment in US debt
  - Covers monthly trade deficit = USD positive
  - Exceeds trade deficit = USD strongly positive
  - Fails to cover deficit = USD bearish
- **Philly Fed Index**: Manufacturing expectations, leading PMI indicator
  - Above 0 = positive for manufacturing = positive for USD
  - Below 0 = negative for manufacturing = negative for USD

### 🌍 Global Economic Indicators
- **CPI (Consumer Price Index)**: Primary inflation metric, all central banks monitor closely
- **Retail Sales**: Leading indicator for GDP correlation
- **PMI (Purchasing Managers' Index)**: Manufacturing activity indicator
- **Housing/Durable Goods**: Correlation for economic outlook
- **Jobless Claims**: Leading unemployment indicator

### 🔗 Fundamental Correlations
- **GDP → Interest Rates**: Economic growth → inflation → rate hikes
- **NFP → Wage Growth**: Employment levels → average hourly earnings → inflation
- **Balance of Trade → Currency Value**: Trade deficit → currency weakness
- **TICS → USD Strength**: Foreign investment → capital inflows → USD strength
- **Philly Fed → PMI**: Manufacturing expectations predict PMI outcomes
- **PPI → CPI**: Producer prices predict consumer inflation (0.85 correlation)
- **Retail Sales → GDP**: Monthly data predicts quarterly GDP (0.78 correlation)
- **ADP → NFP**: Private employment predicts non-farm payrolls (0.80 correlation)
- **Oil Prices → Inflation**: Positive correlation, major input cost factor

### 📰 News Sources Integration
- **Primary**: Bloomberg, FXStreet, ForexFactory
- **Premium**: RanSquid, Lorettatrade ($25/month)
- **Economic Calendars**: Automated tracking of upcoming releases
- **Central Bank Communications**: FOMC, ECB, BoE statements and minutes

### 🛢️ Commodity & Currency Correlations
- **Commodity Currencies**: AUD, NZD positive correlation with commodities
- **AUD → Gold**: Australia = 3rd largest gold producer
- **NZD → Dairy**: Dairy exports significantly impact NZD
- **CAD → Oil**: Canada = 14th largest oil producer, 85% exports to US
- **Safe Havens**: JPY, CHF during political turmoil
- **CHF → Gold**: 25% of Swiss money backed by gold
- **JPY → Oil**: Japan imports most oil, negative correlation with oil prices

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
forex-fundamentals calendar week15,229.17

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

## Monetary Policy Tools

### Central Bank Policy Instruments
- **Interest Rates**: Primary tool for money supply control
  - Higher rates = more expensive borrowing = reduced spending = lower inflation
  - Lower rates = cheaper borrowing = increased spending = higher inflation
- **Reserve Requirements**: Minimum cash banks must hold (not available for lending)
  - Higher requirements = less money available for lending = tighter money supply
  - Lower requirements = more money available for lending = looser money supply
- **Open Market Operations**: Buy/sell bonds to regulate money supply
  - Buying bonds = inject money = expand supply
  - Selling bonds = withdraw money = contract supply

### Key Interest Rates by Region
- **United States**: 
  - Fed Funds Rate: Interbank overnight lending rate
  - Discount Rate: Emergency lending rate (higher than Fed Funds)
- **Eurozone**:
  - Main Refinancing Operations Rate: Primary interbank rate
  - Deposit Facility Rate: Interest on surplus reserves
  - Marginal Lending Facility Rate: Emergency lending rate

### Market Impact Framework
```
Economic Data → Central Bank Assessment → Interest Rate Expectations → Currency Movement
```
- **Positive Data** → Growth/Inflation Concerns → Rate Hike Expectations → Currency Strength
- **Negative Data** → Growth/Inflation Concerns → Rate Cut Expectations → Currency Weakness

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
    "sentiment": "bullish",
    "rate_outlook": "hawkish"
  }
}
```

### Currency Correlation Matrix
```python
{
  "currency_correlations": {
    "EURUSD": {"negative": "USDCHF", "correlation": -0.85},
    "AUDUSD": {"positive": "NZDUSD", "correlation": 0.78},
    "CAD": {"commodity": "oil", "correlation": 0.65},
    "AUD": {"commodity": "gold", "correlation": 0.72},
    "NZD": {"commodity": "dairy", "sensitivity": "high"},
    "CHF": {"safe_haven": True, "gold_backed": 0.25},
    "JPY": {"safe_haven": True, "oil_negative": True}
  }
}
```

### Oil Market Analysis
```python
{
  "opec_influence": {
    "production_share": 0.40,
    "reserve_share": 0.80,
    "middle_east_reserves": 0.85,
    "impact": "production decisions drive global prices"
  },
  "key_importers": ["China", "United States", "Japan", "India"],
  "price_factors": {
    "supply": "US shale production, OPEC decisions",
    "demand": "Chinese economy, energy efficiency",
    "geopolitical": "Middle East stability, sanctions",
    "futures": "hedging activity, speculation",
    "seasonal": "winter heating, summer driving"
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

### Phase 4: Enhanced Integration
- Central bank mandate tracking system
- Currency correlation matrix implementation
- Oil market dynamics integration
- Global economic interconnection analysis
- Advanced monetary policy modeling
- OPEC monitoring and alert system

## Advanced Trading Strategies

### Central Bank Policy Analysis
```bash
# Track central bank meetings and decisions
forex-fundamentals central-bank meetings --fed
forex-fundamentals central-bank mandate --ecb
forex-fundamentals policy-signal --interpret dovish/hawkish

# Analyze inflation targeting across central banks
forex-fundamentals inflation-target --compare fed ecb boe
```

### Currency Correlation Trading
```bash
# Analyze currency correlations for trading opportunities
forex-fundamentals correlation-trading --pairs EURUSD USDCHF
forex-fundamentals commodity-currency --oil-analysis
forex-fundamentals safe-haven-flow --turmoil-detection

# Execute correlation-based trades
forex-fundamentals execute-correlation --buy EURJPY --based EURUSD USDJPY
```

### Oil Market Integration
```bash
# Monitor OPEC decisions and impact
forex-fundamentals opec-monitor --next-meeting
forex-fundamentals oil-impact --currency CAD AUD

# Analyze oil price correlations
forex-fundamentals oil-correlation --global-factors
```

### Global Economic Interconnection
```bash
# Analyze China's impact on commodity currencies
forex-fundamentals china-data --impact AUD NZD

# Monitor US economic influence on global markets
forex-fundamentals us-impact --global-trade-flows
```

## Requirements

- Python 3.8+
- pandas, numpy, requests
- BeautifulSoup4 for web scraping
- Schedule for automated updates
- Optional: News API integration

This skill provides a comprehensive framework for systematic Forex fundamental analysis based on professional trading methodologies.