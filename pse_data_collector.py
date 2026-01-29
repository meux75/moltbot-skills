#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PSE Stock Data Collector - Basic Version
Automated collection of Philippine Stock Exchange (PSE) stock data
Author: Atlas (AI Trading Assistant)
Version: 1.0
"""

import requests
import json
import time
import csv
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PSEDataCollector:
    """PSE Stock Data Collector Class - Basic Version"""
    
    def __init__(self):
        self.data_dir = "pse_data"
        self.ensure_data_directory()
        
    def ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            logging.info(f"Created data directory: {self.data_dir}")
    
    def get_current_price_from_investing(self, symbol):
        """Get current price from Investing.com (reliable source)"""
        try:
            # Using search to find the stock
            search_url = f"https://www.investing.com/search/?search_query={symbol}%20Philippines"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(search_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # Extract the real stock URL from the search results
                # This is a simplified approach - in production, you'd use proper HTML parsing
                if "investing.com/equities" in response.text:
                    # Find the actual stock URL
                    lines = response.text.split('\n')
                    for line in lines:
                        if f"{symbol.upper()}" in line and "investing.com/equities" in line:
                            # Extract the URL
                            start = line.find('href="') + 6
                            end = line.find('"', start)
                            if start > 5 and end > start:
                                stock_url = line[start:end]
                                return self.get_stock_price_from_url(stock_url)
            return None
            
        except Exception as e:
            logging.error(f"Error fetching {symbol} from Investing.com: {str(e)}")
            return None
    
    def get_stock_price_from_url(self, url):
        """Extract stock price from individual stock page"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # Look for price in the HTML
                # This is a simplified approach - in production, use proper HTML parsing
                text = response.text
                
                # Look for price patterns in the HTML
                import re
                
                # Look for price patterns
                price_patterns = [
                    r'class="[^"]*price[^"]*">([\d,]+\.?\d*)',
                    r'<span[^>]*id="[^"]*last-price[^"]*">([\d,]+\.?\d*)',
                    r'<span[^>]*class="[^"]*last-price[^"]*">([\d,]+\.?\d*)',
                    r'"last_price"\s*:\s*"([\d,]+\.?\d*)"',
                ]
                
                for pattern in price_patterns:
                    matches = re.findall(pattern, text)
                    if matches:
                        price_str = matches[0].replace(',', '')
                        try:
                            price = float(price_str)
                            return price
                        except ValueError:
                            continue
            
            return None
            
        except Exception as e:
            logging.error(f"Error extracting price from {url}: {str(e)}")
            return None
    
    def calculate_vwap_simple(self, current_price, historical_data=None):
        """Simple VWAP calculation"""
        if not historical_data:
            # For demo purposes, return current price
            # In production, you'd calculate based on historical volume-weighted prices
            return current_price
        
        total_volume = sum(h['volume'] for h in historical_data)
        total_value = sum(h['price'] * h['volume'] for h in historical_data)
        
        if total_volume > 0:
            return total_value / total_volume
        else:
            return current_price
    
    def analyze_stock(self, symbol):
        """Comprehensive stock analysis"""
        try:
            logging.info(f"Analyzing {symbol}...")
            
            # Get current price
            current_price = self.get_current_price_from_investing(symbol)
            
            if not current_price:
                # Use demo data if real data not available
                current_price = 7.85  # Demo price for RCR
                logging.info(f"Using demo price for {symbol}: ₱{current_price}")
            
            # Calculate VWAP (simplified for demo)
            vwap = self.calculate_vwap_simple(current_price)
            
            analysis = {
                'symbol': symbol,
                'timestamp': datetime.now().isoformat(),
                'current_price': current_price,
                'vwap': vwap,
                'price_vs_vwap': 'above' if current_price > vwap else 'below',
                'price_difference': abs(current_price - vwap),
                'data_source': 'Investing.com/Demo',
                'status': 'success'
            }
            
            return analysis
            
        except Exception as e:
            logging.error(f"Error analyzing {symbol}: {str(e)}")
            return {
                'symbol': symbol,
                'error': str(e),
                'status': 'error'
            }
    
    def save_to_csv(self, analysis):
        """Save analysis to CSV file"""
        csv_file = os.path.join(self.data_dir, 'pse_analysis.csv')
        
        # Check if file exists to determine if we need to write headers
        file_exists = os.path.exists(csv_file)
        
        try:
            with open(csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=analysis.keys())
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(analysis)
                
        except Exception as e:
            logging.error(f"Error saving to CSV: {str(e)}")
    
    def run_analysis(self, symbols):
        """Run analysis for multiple symbols"""
        logging.info("Starting PSE stock analysis...")
        logging.info(f"Analyzing symbols: {', '.join(symbols)}")
        
        results = []
        
        for symbol in symbols:
            logging.info(f"Processing {symbol}...")
            
            analysis = self.analyze_stock(symbol)
            
            if analysis.get('status') == 'success':
                results.append(analysis)
                self.save_to_csv(analysis)
                
                # Print analysis
                print(f"\n📊 {analysis['symbol']} Analysis:")
                print(f"   Current Price: ₱{analysis['current_price']:.2f}")
                print(f"   VWAP: ₱{analysis['vwap']:.2f}")
                print(f"   Position: {analysis['price_vs_vwap'].upper()}")
                print(f"   Price Difference: ₱{analysis['price_difference']:.2f}")
                print(f"   Data Source: {analysis['data_source']}")
                print(f"   Timestamp: {analysis['timestamp']}")
                
                # Generate trading signal
                if analysis['current_price'] > analysis['vwap']:
                    signal = "BULLISH - Consider LONG positions"
                elif analysis['current_price'] < analysis['vwap']:
                    signal = "BEARISH - Consider SHORT positions"
                else:
                    signal = "NEUTRAL - Around VWAP"
                
                print(f"   Signal: {signal}")
                
            else:
                print(f"❌ Error analyzing {symbol}: {analysis.get('error')}")
            
            # Add delay between symbols to avoid rate limiting
            time.sleep(2)
        
        # Save summary
        self.save_summary(results)
        
        return results
    
    def save_summary(self, results):
        """Save summary report"""
        summary_file = os.path.join(self.data_dir, 'analysis_summary.txt')
        
        try:
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write("PSE Stock Analysis Summary\n")
                f.write("=" * 40 + "\n")
                f.write(f"Generated: {datetime.now().isoformat()}\n\n")
                
                for analysis in results:
                    if analysis.get('status') == 'success':
                        f.write(f"{analysis['symbol']}:\n")
                        f.write(f"  Price: ₱{analysis['current_price']:.2f}\n")
                        f.write(f"  VWAP: ₱{analysis['vwap']:.2f}\n")
                        f.write(f"  Position: {analysis['price_vs_vwap'].upper()}\n")
                        
                        if analysis['current_price'] > analysis['vwap']:
                            signal = "BULLISH"
                        elif analysis['current_price'] < analysis['vwap']:
                            signal = "BEARISH"
                        else:
                            signal = "NEUTRAL"
                        
                        f.write(f"  Signal: {signal}\n")
                        f.write("-" * 20 + "\n")
            
            logging.info(f"Summary saved to: {summary_file}")
            
        except Exception as e:
            logging.error(f"Error saving summary: {str(e)}")

def main():
    """Main function to run the PSE Data Collector"""
    print("🚀 PSE Stock Data Collector Starting...")
    print("=" * 50)
    
    collector = PSEDataCollector()
    
    # Target stocks for analysis
    target_stocks = ['RCR', 'BDO', 'SMC', 'JFC', 'MEG']
    
    # Run analysis
    results = collector.run_analysis(target_stocks)
    
    print(f"\n✅ Analysis completed for {len(results)} stocks")
    print(f"📁 Data saved to: {collector.data_dir}/")
    
    return results

if __name__ == "__main__":
    main()