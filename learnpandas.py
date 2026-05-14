import pandas as pd 
import numpy as np 

# This is our source data
data = { 
                 #col
    'Ticker': ['COHR', 'COHR', 'LITE', 'COHR', 'LITE'], #shelf
    'Side': ['Buy', 'Sell', 'Buy', 'Buy', 'Sell'],
    'Price': [252.20, 253.10, 65.50, 252.50, 64.80],
    'Size': [100, 600, 200, 800, 150]
}

# This command creates the 'Warehouse'
df = pd.DataFrame(data)

all_sizes = df['Size']
print(all_sizes)

side =  df['Side'] == 'Buy'
buy_count = 0 
sell_count = 0 

#traditional python for loop 
for side in df['Side']:
    if side == 'Buy':
        buy_count += 1
    else:
        sell_count +=1

print(buy_count, sell_count)


counts = df['Side'].value_counts()
print(counts)

buy_prices = df[df['Side'] == 'Buy']['Price']
print(buy_prices)
buy_market_value = (df[df['Side'] == 'Buy']['Price'] * df['Size']).sum()
print("buy", buy_market_value)

market_value = (df['Size'] * df['Price']).sum()
print(market_value)

data = np.array([[1.5, -0.1, 3], 
                 [0, -3, 6.5]])

data = data * 10
print(data.dtype)
#2rows by 3 cols 

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)