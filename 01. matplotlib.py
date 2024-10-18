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
