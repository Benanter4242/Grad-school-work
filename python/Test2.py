import matplotlib.pyplot as plt
import pandas as pd


degrees = pd.read_csv("CS_degrees.csv",index_col=0)
degrees.plot.box()
plt.savefig("cart.png")
plt.show()
