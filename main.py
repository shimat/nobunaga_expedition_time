import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


def nonlinear_fit(x, a, b, c):
    return b*(x**a) + c


df = pd.read_csv("data.tsv", sep="\t")

x = df["距離[m]"]
y = df["時間(秒換算)"]
p_opt, cov = curve_fit(nonlinear_fit, x, y)
print(p_opt)

y_fit = np.vectorize(nonlinear_fit)

fig, ax = plt.subplots()
ax.set_xlabel("distance[m]")
ax.set_ylabel("time[s]")
ax.plot(x, y, marker="o", label="input data")
ax.plot(x, y_fit(x, *p_opt), label="curve fitting")
ax.grid(axis="both")
ax.legend()
plt.savefig("fig.png")


print(nonlinear_fit(798, *p_opt))