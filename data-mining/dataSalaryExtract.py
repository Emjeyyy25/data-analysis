import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('Dataset-salary-2024.csv')

df.dropna(inplace=True)
df['job_title'] = df['job_title'].astype('str')

df['experience_level'] = df['experience_level'].str.upper()
df['employment_type'] = df['employment_type'].str.upper()
df['salary_currency'] = df['salary_currency'].str.upper()
df['employee_residence'] = df['employee_residence'].str.upper()
df['company_location'] = df['company_location'].str.upper()
df['company_size'] = df['company_size'].str.upper()

df['work_year'] = df['work_year'].astype(int)
df['salary'] = df['salary'].astype(float)
df['remote_ratio'] = df['remote_ratio'].astype(int)

Q1 = df['salary_in_usd'].quantile(0.25)
Q3 = df['salary_in_usd'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['salary_in_usd'] >= lower_bound) & (df['salary_in_usd'] <= upper_bound)]

engine = create_engine('sqlite:///salary2024.db')
df.to_sql('software_engineer', engine, if_exists='replace', index=False)

print("Data has been successfully processed and stored in the database.")
