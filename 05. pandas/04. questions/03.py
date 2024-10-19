"""
Insert the row ['11/2/2011', 'Wrestling', 12000] at position 1 in Pandas Dataframe

data = {
    'Date':['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
    'Cost':[10000, 5000, 15000, 2000]
}
"""
import pandas as pd
data = {
    'Date':['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
    'Cost':[10000, 5000, 15000, 2000]
}
def insert_row(i, value, df):
    df1 = df.loc[:i].copy()
    df2 = df.loc[i:]
    df1.loc[i] = value
    new_df = pd.concat([df1, df2])
    new_df.reset_index(inplace=True, drop=True)
    return new_df

df = pd.DataFrame(data)
i = 1
value = ['11/2/2011', 'Wrestling', 12000]
df = insert_row(i, value, df)
print(df)


"""
Ranking Rows of Pandas DataFrame
data = {
    'Name': ['The Godfather', 'Bird Box', 'Fight Club'], 
    'Year': ['1972', '2018', '1999'], 
    'Rating': ['9.2', '6.8', '8.8']
}
"""
import pandas as pd 
data = {
    'Name': ['The Godfather', 'Bird Box', 'Fight Club'], 
    'Year': ['1972', '2018', '1999'], 
    'Rating': ['9.2', '6.8', '8.8']
} 
df = pd.DataFrame(data)
df['Rank'] = df['Rating'].rank(ascending = 1).astype(int)
print(df) 


"""
How to select rows randomly
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
df = pd.DataFrame(data)
print(df.sample(1))


"""
How to rename columns in Pandas DataFrame
data = {
    'test': ['India', 'South Africa', 'England', 'New Zealand', 'Australia'],
    'odi': ['England', 'India', 'New Zealand', 'South Africa', 'Pakistan'],
    't20': ['Pakistan', 'India', 'Australia', 'England', 'New Zealand']
}
"""
import pandas as pd
data = {
    'test': ['India', 'South Africa', 'England', 'New Zealand', 'Australia'],
    'odi': ['England', 'India', 'New Zealand', 'South Africa', 'Pakistan'],
    't20': ['Pakistan', 'India', 'Australia', 'England', 'New Zealand']
}
df = pd.DataFrame(data)
df.rename(columns = {'test':'TEST'}, inplace = True)
print(df)


"""
Get unique values from a column in Pandas DataFrame
data = { 
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] 
}
"""
import pandas as pd 
data = { 
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] 
} 
df = pd.DataFrame(data) 
unique_values = df.B.unique() 
print(unique_values)


"""
Using dictionary to replace row values
data = {
    'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
    'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
    'Cost': [10000, 5000, 15000, 2000]
}
"""
import pandas as pd
data = {
    'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
    'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
    'Cost': [10000, 5000, 15000, 2000]
}
df = pd.DataFrame(data)
dict = {'Music' : 'M', 'Poetry' : 'P', 'Theatre' : 'T', 'Comedy' : 'C'}
df.replace({"Event": dict}, inplace=True)
print(df)


"""
Split the string into columns using regex in pandas dataframe
data = ["Name: The_Godfather Year: 1972 Rating: 9.2", 
        "Name: Bird_Box Year: 2018 Rating: 6.8", 
        "Name: Fight_Club Year: 1999 Rating: 8.8"]
"""
import pandas as pd
import re

data = ["Name: The_Godfather Year: 1972 Rating: 9.2", 
        "Name: Bird_Box Year: 2018 Rating: 6.8", 
        "Name: Fight_Club Year: 1999 Rating: 8.8"]

rows = {"Name":[], "Year":[], "Rating":[]}
for ele in data:
    name = re.search("(?<=Name:\s)[a-zA-Z_]+", ele)
    rows["Name"].append(name.group())
    year = re.search("(?<=Year:\s)[0-9]+", ele)
    rows["Year"].append((year.group()))
    rating = re.search("(?<=Rating:\s)[0-9.]+", ele)
    rows["Rating"].append(rating.group())

df = pd.DataFrame(rows)
print(df)