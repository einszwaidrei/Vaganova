import pandas as pd
import math

file = 'vacancies_dif_currencies.csv'
df = pd.read_csv(file)
df_currencies = pd.read_csv('data_currencies.csv')
df.insert(1, 'salary', None)
for row in df.itertuples():
    salary_from = row.salary_from
    salary_to = row.salary_to
    salary_currency = row.salary_currency
    salary = row.salary
    if type(salary_currency) is str:
        if not math.isnan(salary_from) and not math.isnan(salary_to):
            salary = (salary_from + salary_to) / 2
        elif not math.isnan(salary_from):
            salary = salary_from
        elif not math.isnan(salary_to):
            salary = salary_to
        if salary_currency != 'RUR' and salary_currency in ['BYR', 'USD', 'EUR', 'KZT', 'UAH']:
            ratio_currency = df_currencies[df_currencies['date']
                                           == f'01/{row.published_at[5:7]}/{row.published_at[:4]}'][
                salary_currency].values[0]
            salary = None if math.isnan(ratio_currency) else salary * ratio_currency
        elif salary_currency != 'RUR':
            salary = None
        df.at[df.index[int(row.Index)], 'salary'] = salary
    print(df.index[int(row.Index)])
df.pop('salary_from')
df.pop('salary_to')
df.pop('salary_currency')
df.to_csv('vacancies_result.csv', index=False)