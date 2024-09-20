import pandas as pd
from datetime import datetime

df = pd.read_csv('Data/data.csv')

df.loc[0, 'month'] = datetime.now().strftime('%B %Y')
# convert month to datetime month and year
df['month'] = pd.to_datetime(df['month'], format='%B %Y')


def calc_pct(avg_month, monthly_change):
    return (monthly_change / avg_month) * 100

df["monthly_change_pct_fixed"] = df.apply(lambda x: calc_pct(x.avg_month, x.monthly_change), axis=1)

print(df.head())
df.to_csv('Data/data_clean.csv', index=False)