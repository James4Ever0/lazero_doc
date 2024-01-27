import pandas as pd


def get_writings():
    p = pd.read_csv("mnist-demo.csv")
    # print(dir(p))
    dp = p.to_numpy()
    # not for label!
    return dp[:, :1], dp[:, 1:]
# print(dp.shape)
# print(dp[0])
# this solution is just for some estimation.
# solving the equation.
# problem is, that you do not have bias.
# it is not complex enough.