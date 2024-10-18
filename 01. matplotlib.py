"""
Matplotlib is an open-source Python library built for data visualization that lets you produce a wide 
variety of highly customizable charts & graphs
"""

"""
Basic Plot
X axis is index values
Y axis is list values
"""
import matplotlib.pyplot as plt

plt.plot([0,1,4,9,16,25])
plt.show()


"""
Compatible Data Types
"""
import matplotlib.pyplot as plt
import pandas as pd

data = [x*10 for x in range(10)]
labels = [f"{x}!" for x in range(10)]
df = pd.DataFrame(data, labels).assign(series2=lambda x: x[0]/2)
plt.plot(df)
plt.show()


"""
Object Oriented Plotting
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
Plotting Dataframes
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

import matplotlib.pyplot as plt
import pandas as pd

hotels = pd.read_excel("./HotelCustomersDataset.xlsx")
hotels["date"] = (
    pd.to_datetime("2018-12-31") - pd.to_timedelta(hotels["DaysSinceCreation"], unit="D")
)
daily_revenue = hotels.groupby("date").agg({"LodgingRevenue":"sum", "OtherRevenue":"sum"})
monthly_revenue = daily_revenue.resample("ME").sum()

fig, ax = plt.subplots()
ax.plot(monthly_revenue.index, monthly_revenue["LodgingRevenue"])
ax.plot(monthly_revenue.index, monthly_revenue["OtherRevenue"])
plt.show()
