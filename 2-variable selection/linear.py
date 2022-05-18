# %%
from sklearn.linear_model import Lasso
import abess
import pandas as pd
import numpy as np
data = pd.read_csv("data8.csv")
data.head()
vars = data.drop(columns=['city', '年份', 'score'])

# %% lasso
model = Lasso(alpha=50000)
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

# %%
