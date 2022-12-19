import pandas as pd
import requests as requests

file = 'vacancies_dif_currencies.csv'
df=pd.read_csv(file)
currencies=df['salary_currency'].unique()
currency_list=[]
df.sort_values(by='published_at',inplace=True)
for cur in currencies:
    if list(df['salary_currency']).count(cur)>5000:
        currency_list.append(cur)
del currency_list[0]
first_date=list(df['published_at'])[0]
end_date=list(df['published_at'])[-1]
print(currency_list)

data=pd.DataFrame(columns=['date','BYR','USD','EUR','KZT','UAH'])
for year in range (2003,2023):
    for month in range(1,13):
        if month==1 and year==2003:
            date='24/01/2003'
        elif month==7 and year==2022:
            date = '19/07/2022'
        else:
            date= f'01/0{month}/{year}' if month<10 else f'01/{month}/{year}'
        res = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
        new_row={'date':date}
        values_cur = pd.read_xml(res, encoding='cp1251')
        for cur in currency_list:
            if len(values_cur[values_cur['CharCode']==cur]['Value'].values)!=0:
                value='.'.join(str(values_cur[values_cur['CharCode'] == cur]['Value'].values[0]).split(','))
                new_row[cur]=float(value) / int(values_cur[values_cur['CharCode'] == cur]['Nominal'].values[0])
        data=pd.concat([data, pd.DataFrame.from_records([new_row])], axis=0,ignore_index=True)
        if date=='19/07/2022':
            break
data.to_csv('data_currencies.csv', index=False)
