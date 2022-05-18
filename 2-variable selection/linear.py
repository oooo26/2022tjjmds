# %%
from sklearn.linear_model import Lasso
import abess
import pandas as pd
import numpy as np
data = pd.read_csv("data8.csv")
data.head()
vars = data.drop(columns=['city', '年份', 'score'])
vars = (vars - vars.mean()) / vars.std()

# %% lasso
model = Lasso(alpha=0.15)
model.fit(vars, data['score'])
print(np.count_nonzero(model.coef_))

ind= np.nonzero(model.coef_)
print(vars.columns[ind])

# %% abess
model = abess.LinearRegression(support_size = range(14), ic_type='bic')
model.fit(vars, data['score'])
print(np.count_nonzero(model.coef_))

ind= np.nonzero(model.coef_)
print(vars.columns[ind])

# %% save
new_data = pd.concat([data[['city', '年份', 'score']], vars[vars.columns[ind]]], axis=1)
new_data.to_csv("./selected.csv", index=False)
