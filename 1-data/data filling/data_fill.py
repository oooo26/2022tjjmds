# %%
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import warnings


warnings.filterwarnings("ignore")

file = "data6"
data = pd.read_csv(f"./{file}.csv")
cities = set(data['city'])
columns = data.columns
print(cities)

# %%
for city in cities:
    dt = data.loc[data['city'] == city].copy()
    x_cols = columns[~dt.isna().any()].drop('city')
    y_cols = columns[dt.isna().any()]

    print(f"Filling {city}'s data:")
    # x = dt[[
    #     '年份',
    #     '年末户籍总人口',
    #     '全市生产总值（按当年价计算）  （万元）',
    #     '进出口总值（万美元）',
    #     '增值税'
    # ]].copy()
    x = dt[x_cols].copy()
    for col in y_cols:
        y = dt[col].copy()
        ind = y.isna()
        pipe = make_pipeline(
            StandardScaler(),
            Lasso()
        )
        pipe.fit(x.loc[~ind], y.loc[~ind])
        y.loc[ind] = pipe.predict(x.loc[ind])
        dt[col] = y
        print(f"  ==> {col}\t done.")

    data[data['city'] == city] = dt

if not data.isna().any().any():
    print("All filled.")

# %%
data.to_csv(f"./{file}_fill.csv", index=False)

# %%
