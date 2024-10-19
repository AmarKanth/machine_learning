"""
Getting frequency counts of a columns in Pandas DataFrame
data = {
    'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g', 'bar', 'bar', 'foo', 'bar'], 
    'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b']
}
"""
import pandas as pd 

data = {
    'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g', 'bar', 'bar', 'foo', 'bar'], 
    'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b']
}

df = pd.DataFrame(data)
count = df['A'].value_counts() 
print(count) 


"""
Get the index of maximum value in DataFrame column
https://media.geeksforgeeks.org/wp-content/uploads/nba.csv
"""
import pandas as pd 

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
index = df[['Weight']].idxmax()
print(index)


"""
Get the 5 largest values in DataFrame column 
https://media.geeksforgeeks.org/wp-content/uploads/nba.csv
"""
import pandas as pd 

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
res = df.nlargest(5, ['Age']) 
print(res)


"""
Drop Columns from a Dataframe
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']
}
"""
import pandas as pd

data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']
}

df = pd.DataFrame(data)
df.drop(['A'], axis=1, inplace=True)
print(df)


"""
create DateTime based indexes in Pandas
data =  {
    'City':['Lisbon', 'Parague', 'Macao', 'Venice'], 
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
    'Cost':[10000, 5000, 15000, 2000]
}
"""
import pandas as pd

data =  {
    'City':['Lisbon', 'Parague', 'Macao', 'Venice'], 
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
    'Cost':[10000, 5000, 15000, 2000]
}
df = pd.DataFrame(data)
index_ = [pd.Timestamp('01-06-2018'), pd.Timestamp('04-06-2018'), 
          pd.Timestamp('07-06-2018'), pd.Timestamp('10-06-2018')] 

df.index = index_ 
print(df)


"""
Convert the column type from string to datetime format in Pandas dataframe
data = {
    'Date':['11/8/2011', '04/23/2008', '10/2/2019'],
    'Event':['Music', 'Poetry', 'Theatre'],
    'Cost':[10000, 5000, 15000]
}
"""
import pandas as pd

data = {
    'Date':['11/8/2011', '04/23/2008', '10/2/2019'],
    'Event':['Music', 'Poetry', 'Theatre'],
    'Cost':[10000, 5000, 15000]
}
df = pd.DataFrame(data)
df['Date']= pd.to_datetime(df['Date'])
print(df.info())


"""
Transform the department table by month and value as Revenue
data = {
    "id": [1,2,3,1,1],
    "revenue": [8000, 9000, 10000, 7000, 6000],
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar"]
}
"""
import calendar
import pandas as pd

data = {
    "id": [1,2,3,1,1],
    "revenue": [8000, 9000, 10000, 7000, 6000],
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar"]
}
department = pd.DataFrame(data)
df = department.pivot(index="id", columns="month", values="revenue").add_suffix("_Revenue").reset_index()
new_columns = ['id'] + [f"{month}_Revenue" for month in list(calendar.month_abbr)[1:]]
df = df.reindex(columns=new_columns)
print(df)
