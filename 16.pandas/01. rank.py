"""
184 Department highest salary
"""
emp_data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], 
			[5, 'Max', 90000, 1]]
employee = pd.DataFrame(emp_data, columns=['id', 'name', 'salary', 'departmentId']).astype(
	{'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})

dept_data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(dept_data, columns=['id', 'name']).astype(
	{'id':'Int64', 'name':'object'})

grouped_df = employee.groupby(by=["departmentId"])
employee["rnk"] = grouped_df["salary"].rank(method="dense", ascending=False).astype(int)
filtered_df = employee[employee["rnk"] == 1]
df = pd.merge(filtered_df, department, left_on="departmentId", right_on="id", how="inner")
df.rename(columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}, inplace=True)
df[["Department", "Employee", "Salary"]]