
import pandas as pd
from matplotlib import pyplot as plt

# Read the stock data
def read_and_normalize_data(csv_file):
    data = pd.read_csv(csv_file)
    data['Close'] = pd.to_numeric(data['Close'],errors='coerce')
    data['Normalized'] = data['Close']/data['Close'].iloc[0]
    return data

print('Reading and normalizing AAPL stock data...')
aapl_data = read_and_normalize_data('aapl_data.csv')

print('Reading and normalizing META stock data...')
meta_data = read_and_normalize_data('meta_data.csv')

# Plot the normalized data
print('Generating plot...')
plt.figure(figsize=(12,8))
plt.plot(aapl_data['Date'], aapl_data['Normalized'], label='AAPL')
plt.plot(meta_data['Date'], meta_data['Normalized'], label='META')
plt.xlabel('Date')
plt.ylabel('Normalized Prices')
plt.title('Normalized Stock Prices of AAPL and META for the last 1 year')
plt.legend()
plt.grid()
plt.savefig('stock_prices_plot.png')
