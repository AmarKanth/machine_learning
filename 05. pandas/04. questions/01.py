"""
input_data = { 
    "emp": ["A", "B", "C", "D", "E", "F", "G"], 
    "sal": [1000, 2000, 3000, 4000, 2000, 1500, 7000], 
    "dept": ["IT", "IT", "IT", "HR", "HR", "IT", "HR"],
} 
add a column next highest salary in same department. Output should be like this 
{
    'emp': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 
    'sal': [1000, 2000, 3000, 4000, 2000, 1500, 7000], 
    'dept': ['IT', 'IT', 'IT', 'HR', 'HR', 'IT', 'HR'], 
    'sec_high_sal': [1500, 3000, '-', 7000, 4000, 2000, '-']
} 
"""
import pandas as pd

data = { 
    "emp": ["A", "B", "C", "D", "E", "F", "G"], 
    "sal": [1000, 2000, 3000, 4000, 2000, 1500, 7000], 
    "dept": ["IT", "IT", "IT", "HR", "HR", "IT", "HR"],
} 

def sec_high_sal(row, df):
    filtered_df = df[(df["sal"] > row.sal) & (df["dept"] == row.dept)]
    if filtered_df.empty:
        return "-"
    return filtered_df.sort_values(by=["sal"]).iat[0,1]

df = pd.DataFrame(data)
df["sec_high_sal"] = df.apply(sec_high_sal, args=(df,), axis=1)
print(df)


"""
Create data frame with Exam,Grade,Name using given input data
lst = [{
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                ],
        "Name": "Paras Jain"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                ],
        "Name": "Chunky Pandey"
        }
    ]
"""
import pandas as pd

lst = [{
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                ],
        "Name": "Paras Jain"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                ],
        "Name": "Chunky Pandey"
        }
    ]

rows = []

for data in lst:
    students = data["Student"]
    for student in students:
        student["Name"] = data["Name"]
        rows.append(student)

df = pd.DataFrame.from_records(rows)
print(df)


"""
Replace values in Pandas dataframe using regex
data = {
    'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
    'Cost':[10000, 5000, 15000, 2000, 12000]
}
"""
import pandas as pd

data = {
    'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
    'Cost':[10000, 5000, 15000, 2000, 12000]
}
_index = [pd.Period('02-2018'), pd.Period('04-2018'), pd.Period('06-2018'), pd.Period('10-2018'), 
          pd.Period('12-2018')]

df = pd.DataFrame.from_records(data, index=_index)
df.replace(to_replace ='[nN]ew', value = 'New', regex = True, inplace=True)
print(df)