"""
Line Style
"""
import pandas as pd
import matplotlib.pyplot as plt

housing_raw = pd.read_csv(
    "./data_science/04. matplotlib/data/housing_data.csv",
    parse_dates=["period_begin", "period_end"],
    dtype={"region_name":"category"}
)

ca_housing = housing_raw.loc[
    housing_raw["region_name"].str.contains('CA')
].assign(region_name=housing_raw["region_name"].str[0:-11])

ca_housing_pivot = ca_housing.pivot_table(index="period_begin", columns="region_name", values="median_active_list_price"
).assign(CA_average=lambda x: x.mean(axis=1))

ca_housing_markets = ca_housing_pivot.loc[:, ["San Francisco", "Los Angeles", "San Diego", "CA_average"]]

fig, ax = plt.subplots()

ax.plot(ca_housing_markets.index, ca_housing_markets["San Francisco"], label="San Francisco", color="red", linewidth=2)
ax.plot(ca_housing_markets.index, ca_housing_markets["Los Angeles"], label="Los Angeles", color="black", ls=":")

ax.set_title("Housing Prices in CA Markets 2017-2022", fontsize=12)
ax.set_xlabel("Year")
ax.set_ylabel("Price (Millions)")
ax.legend(bbox_to_anchor=(1, -.08), ncol=3, frameon=False)

plt.show()
