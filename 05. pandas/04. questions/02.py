"""
Construct a DataFrame in Pandas using string data
Date;Event;Cost
10/2/2011;Music;10000
11/2/2011;Poetry;12000
12/2/2011;Theatre;5000
13/2/2011;Comedy;8000
"""
import pandas as pd
from io import StringIO

StringData = StringIO("""Date;Event;Cost
    10/2/2011;Music;10000
    11/2/2011;Poetry;12000
    12/2/2011;Theatre;5000
    13/2/2011;Comedy;8000
    """)

df = pd.read_csv(StringData, sep =";")
print(df)


"""
Clean the string data in the given Pandas Dataframe
data = {
    'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
    'Product':[' UMbreLla', ' maTtress', 'BaDmintoN ', 'Shuttle'],
    'Updated_Price':[1250, 1450, 1550, 400],
    'Discount':[10, 8, 15, 10]
}
"""
import pandas as pd

data = {
    'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
    'Product':[' UMbreLla', ' maTtress', 'BaDmintoN ', 'Shuttle'],
    'Updated_Price':[1250, 1450, 1550, 400],
    'Discount':[10, 8, 15, 10]
}

df = pd.DataFrame(data)
df['Product'] = df['Product'].apply(lambda x : x.strip().capitalize())
print(df)


"""
Reindexing in Pandas DataFrame
column=['a','b','c','d','e']
index=['A','B','C','D','E']
"""
import pandas as pd
import numpy as np
 
column=['a','b','c','d','e']
index=['B', 'D', 'A', 'C', 'E']

df = pd.DataFrame(np.random.rand(5,5), columns=column, index=index)
print(df) 
df = df.reindex(['A','B','C','D','E'])
print(df)


"""
Mapping external values to dataframe values in Pandas
data = {
    'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
    'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
    'Age': [42, 52, 36, 21, 23],
    'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']
}
"""
import pandas as pd

data = {
    'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
    'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
    'Age': [42, 52, 36, 21, 23],
    'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']
}

df = pd.DataFrame(data)
new_data = { "Ram":"B.Com", "Mohan":"IAS", "Tina":"LLB", "Jeetu":"B.Tech", "Meera":"MBBS"}
df["Qualification"] = df["First_name"].map(new_data)
print(df)


"""
Reshape a pandas DataFrame using stack,unstack
source url is https://media.geeksforgeeks.org/wp-content/uploads/nba.csv
"""
import pandas as pd

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
print(df)
df_stacked = df.stack()
print(df_stacked)
df_unstacked = df_stacked.unstack()
print(df_unstacked)


"""
Reset Index in Pandas Dataframe
data = {
    'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
    'Age':[27, 24, 22, 32, 15],
    'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
    'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']
}
"""
import pandas as pd

data = {
    'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
    'Age':[27, 24, 22, 32, 15],
    'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
    'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']
}

index = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data, index)
df.reset_index(inplace = True)
print(df)


"""
How to iterate over rows in Pandas Dataframe
data = [{'name':'Sujeet', 'age':10},
        {'name':'Sameer', 'age':11},
        {'name':'Sumit', 'age':12}
]
"""
import pandas as pd

data = [{'name':'Sujeet', 'age':10},
        {'name':'Sameer', 'age':11},
        {'name':'Sumit', 'age':12}
]

df = pd.DataFrame(data)
for index, row in df.iterrows():
    print(row['name'], row['age'])