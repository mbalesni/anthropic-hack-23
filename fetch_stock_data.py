
import os
import pandas as pd
import yfinance as yf

def download_stock_data(ticker, start_date, end_date, csv_file):
    stock_data = yf.download(tickers=ticker, start=start_date, end=end_date)
    stock_data.to_csv(csv_file)

# Download AAPL data
print('Downloading AAPL stock prices...')
download_stock_data('AAPL', '2021-11-01', '2022-11-01', 'aapl_data.csv')

# Download META data
print('Downloading META stock prices...')
download_stock_data('META', '2021-11-01', '2022-11-01', 'meta_data.csv')
