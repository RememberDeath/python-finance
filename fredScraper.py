from fredapi import Fred
import pandas as pd

fred = Fred(api_key='57c0af0784604f937d25082bbae24404')

ten_year = fred.get_series('GS10')

two_year = fred.get_series('GS2')

df = pd.DataFrame({'10 Year': ten_year, '2 Year': two_year})

df['Spread'] = df['10 Year'] - df['2 Year']

print(df.tail(10))

import matplotlib.pyplot as plt

df['Spread'].plot(title='2s10s Treasury Spread', figsize=(10,5))
plt.axhline(0, color='red', linestyle='--')
plt.ylabel('Spread (percentage points)')
plt.show()