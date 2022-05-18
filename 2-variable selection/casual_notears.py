# %%
import pandas as pd
import numpy as np
data = pd.read_csv("data8.csv")
data.head()
vars = data.drop(columns=['city', '年份', 'score']).to_numpy()

# %%
from notears import utils, linear
utils.set_random_seed(1)
adjmat = linear.notears_linear(vars, lambda1=0.1, loss_type='l2')
np.save("casual_notears.npy", adjmat)
