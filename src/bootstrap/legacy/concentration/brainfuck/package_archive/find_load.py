import pandas as pd
s = "/usr/local/lib/python3.8/dist-packages/sklearn/datasets/data/boston_house_prices.csv"
lf = pd.read_csv(s)
n = 5
# col_name=lf.iloc[n]
col_name = lf.iloc[0]
# col_name=lf.iloc[n,0]
# print(col_name)
# dt=lf.iloc[0:]
dt = lf.iloc[1:]
# print(dir(dt))
# print(dt.to_numpy())
dt = dt.to_numpy()
print(dt)
# print(dt.transform(-1,4))
# print(dt.astype("float64").T)
# print(dt.transpose(1,0))
# maybe no difference.
print(dt.swapaxes(1,0))
print(dt.swapaxes(0,1))
# yes! no fucking difference.
# i guess it is the order of axes.