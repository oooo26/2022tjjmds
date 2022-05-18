# %%
from sklearn.decomposition import SparsePCA
import abess
import pandas as pd
import numpy as np
data = pd.read_csv("data8.csv")
data.head()
vars = data.drop(columns=['city', '年份', 'score'])

# %% sklearn - lars
model = SparsePCA(n_components=1, random_state=0, alpha=6000000, method="lars")
model.fit(vars)
print(np.count_nonzero(model.components_))

ind= np.nonzero(model.components_)[1]
print(vars.columns[ind])

# %% sklearn - cd
model = SparsePCA(n_components=1, random_state=0, alpha=6000000, method="cd")
model.fit(vars)
print(np.count_nonzero(model.components_))

ind= np.nonzero(model.components_)[1]
print(vars.columns[ind])

# %% abess
model = abess.SparsePCA(support_size=np.ones((10, 1)))
model.fit(vars)
print(np.count_nonzero(model.coef_))

ind= np.nonzero(model.coef_)[0]
print(vars.columns[ind])
