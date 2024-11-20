import numpy as np
import pandas as pd


data = pd.Series(np.random.uniform(size=9),
index=[["a", "a", "a", "b", "b", "c", "c", "d", "d"],
[1, 2, 3, 1, 3, 1, 2, 2, 3]])


print(data)