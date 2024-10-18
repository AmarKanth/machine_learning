"""
Basic Plot
X axis is index values
Y axis is list values
"""
import matplotlib.pyplot as plt

plt.plot([0,1,4,9,16,25])
plt.show()

"""
Matplotlib with pandas
"""
import matplotlib.pyplot as plt
import pandas as pd

data = [x*10 for x in range(10)]
labels = [f"{x}!" for x in range(10)]

df = pd.DataFrame(data, labels).assign(series2=lambda x: x[0]/2)
plt.plot(df)
plt.show()

"""
Subplots
"""
import matplotlib.pyplot as plt
import pandas as pd

data = [x*10 for x in range(10)]
labels = [f"{x}!" for x in range(10)]

df = pd.DataFrame(data, labels).assign(series2=lambda x: x[0]/2)

fig, ax = plt.subplots()
ax.plot(df)
ax.set_title("Title")
fig.suptitle("Overall Title")

plt.show()

"""
Format Plotting
"""
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Sales": [10, 20, 30, 40],
    "Profiles": [2, 4, 3, 1],
    "Date": ["2022-01-01", "2022-02-01", "2022-03-01", "2022-04-01"]
}

df = pd.DataFrame(data, columns=["Sales", "Profiles"], index=data["Date"])

fig, ax = plt.subplots()
ax.plot(df.index, df["Sales"])
ax.plot(df.index, df["Profiles"], ls="--")
ax.set_title("Product Sales And Profits")
plt.show()
