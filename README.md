# Forex Fundamental Analysis Skill

A comprehensive skill for Forex fundamental analysis based on professional trading strategies. This skill provides tools for economic data analysis, market sentiment tracking, and systematic fundamental trading.

## 🌍 Overview

This skill implements the professional Forex fundamental analysis methodology you learned, combining session analysis, economic calendar tracking, correlation analysis, and market sentiment monitoring to create actionable trading signals.

## 📁 Files Structure

```
forex-fundamentals/
├── SKILL.md                    # Main skill documentation
├── README.md                   # This file
├── TRADINGVIEW_STRATEGY_GUIDE.md # Pine Script implementation guide
├── PINE_SCRIPT_V6_FIX.md      # Version 6 compatibility fixes
├── config.json                # Skill configuration
├── package.json               # Package metadata
├── requirements.txt           # Python dependencies
├── forex-fundamentals          # CLI executable
├── forex-fundamental-analysis-strategy-v6-fully-fixed.pinescript  # Main strategy
├── forex-fundamental-flags-indicator-v6-fully-fixed.pinescript   # Indicator
└── LOCATION_UPDATE.md         # Location information
```

## 🚀 Features

### 1. Market Session Analysis
- **24/5 Forex Market**: New York, Tokyo, Sydney, London sessions
- **Session Overlaps**: Identify optimal trading times (8-11am EST: London/New York, 19-1am EST: Sydney/Tokyo)
- **Liquidity Analysis**: Track market participation levels

### 2. Economic Calendar Integration
- **High-Impact Events**: NFP, CPI, Interest Rate Decisions
- **Medium-Impact Events**: Retail Sales, GDP, PMI
- **Custom Filtering**: By country, impact level, and indicator type

### 3. Correlation Analysis
- **PPI → CPI**: Producer price index predicts consumer inflation (0.85 correlation)
- **Retail Sales → GDP**: Monthly data predicts quarterly GDP (0.78 correlation)
- **ADP → NFP**: Private sector employment predicts non-farm payrolls (0.80 correlation)

### 4. Market Sentiment Tracking
- **Risk-on/risk-off Detection**: Market mood analysis
- **Safe Haven Flows**: USD, JPY performance monitoring
- **Institutional Order Flow**: Large order simulation

### 5. Central Bank Focus
- **Federal Reserve**: Dual mandate (inflation + employment)
- **ECB/BoJ/BoE**: Price stability focus
- **Policy Direction**: Interest rate and quantitative easing analysis

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager
- Optional: uv (faster package management)

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd forex-fundamentals

# Install dependencies
pip install -r requirements.txt

# Alternative with uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
uv pip install -r requirements.txt

# Make executable
chmod +x forex-fundamentals
```

## 📊 Usage

### CLI Commands
```bash
# Market overview
./forex-fundamentals market-overview

# Economic calendar
./forex-fundamentals calendar today
./forex-fundamentals calendar --country US --high-impact
./forex-fundamentals calendar week

# Currency analysis
./forex-fundamentals outlook USD
./forex-fundamentals outlook EUR

# Correlation analysis
./forex-fundamentals correlate PPI CPI
./forex-fundamentals correlate RetailSales GDP

# Market sentiment
./forex-fundamentals sentiment

# Trading signals
./forex-fundamentals signals
```

### Configuration
Edit `config.json` to customize:
- Data sources and update frequencies
- Economic indicator impact levels
- Correlation thresholds
- Trading session preferences

## 🎯 TradingView Integration

### Main Strategy
File: `forex-fundamental-analysis-strategy-v6-fully-fixed.pinescript`

**Features:**
- Automated entry/exit signals
- Risk management with customizable stops
- Session overlap trading
- Correlation confirmation
- Market sentiment alignment

**Usage:**
1. Copy to TradingView Pine Editor
2. Apply to 4H timeframe
3. Configure inputs
4. Enable alerts for signal notifications

### Indicator
File: `forex-fundamental-flags-indicator-v6-fully-fixed.pinescript`

**Features:**
- Visual entry/exit flags
- Real-time correlation display
- Session activity background
- Support/resistance levels
- Market sentiment indicators

**Usage:**
1. Copy to TradingView Pine Editor
2. Apply as overlay
3. Use for manual trading signals
4. Monitor correlation strength

## 🔧 Customization

### Adding New Economic Indicators
1. Update `config.json` with new indicator definitions
2. Modify correlation logic in the CLI tool
3. Update Pine Script strategy if needed

### Session Configuration
- Modify session times in `config.json`
- Add new session overlap periods
- Customize liquidity thresholds

### Risk Management
- Adjust position sizing parameters
- Modify stop-loss rules
- Configure risk/reward ratios

## 📈 Performance Optimization

### Timeframes
- **4H**: Optimal for fundamental analysis
- **Daily**: For trend following
- **1H**: For active session trading

### Currency Pairs
- **Majors**: EUR/USD, GBP/USD, USD/JPY
- **Commodity**: AUD/USD, USD/CAD
- **Crosses**: EUR/GBP, AUD/JPY

### Economic Events
- **High Impact**: NFP, CPI, Interest Rate decisions
- **Medium Impact**: Retail Sales, GDP, PMI
- **Low Impact**: Balance of Trade, Manufacturing Orders

## 🚨 Important Notes

- **Backtesting**: Always test on historical data before live trading
- **Risk Management**: Use appropriate position sizing and stop-losses
- **News Sources**: Monitor economic calendars for real-time updates
- **Session Times**: Adjust for your local timezone
- **Correlation Quality**: Monitor correlation strength regularly

## 📝 Documentation

- **SKILL.md**: Complete skill documentation and API reference
- **TRADINGVIEW_STRATEGY_GUIDE.md**: Detailed Pine Script implementation guide
- **PINE_SCRIPT_V6_FIX.md**: Version 6 compatibility and troubleshooting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🔗 Support

For issues and questions:
- Check the documentation files
- Review the TradingView strategy guide
- Test in a demo environment before live trading

---

**Forex Fundamental Analysis Skill** - Professional-grade fundamental analysis tools for systematic Forex trading based on proven methodologies.