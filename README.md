# Vaganova
Юнит-тесты
![image](https://user-images.githubusercontent.com/97828035/205136913-3c31c19e-358c-4da8-a6b5-4c969f5e7d09.png)

Доктесты
![2022-12-02_00-03-29](https://user-images.githubusercontent.com/97828035/205138035-627002ef-ce98-4d58-a893-77c70b2990ec.png)


Профилизатор в Pycharm. Задание 2.3.3
Запустили профилизатор на исходном коде
![первыйзапуск](https://user-images.githubusercontent.com/97828035/206177281-8d94bec5-b915-4556-84e8-0bf140a42598.jpg)
Метод форматирования даты оказался самым долгим, рассмотрим 3 его вариации:
1 вариация
```py
def change_data(date_vac):
            """
            Форматирует дату к читабельному формату

            Arguments:
                date_vac (str): Дата публикации
            returns:
                str: Отформатированная строка даты
            :return:
            """
            return datetime.datetime.strptime(date_vac, '%Y-%m-%dT%H:%M:%S%z').strftime('%d.%m.%Y')
```
Результаты профилизатора представлены в скриншоте выше

2 вариация
```py
from dateutil.parser import parse
def change_data(date_vac):
            """
            Форматирует дату к читабельному формату

            Arguments:
                date_vac (str): Дата публикации
            returns:
                str: Отформатированная строка даты
            :return:
            """
            return parse(date_vac).strftime('%d.%m.%Y')
```            
Результаты профилизатора: ![второй запуск](https://user-images.githubusercontent.com/97828035/206178680-41e19e22-1195-490b-b28c-187b76754e03.jpg)
Метод стал выполняться еще дольше


3 вариация
```py
 def change_data(date_vac):
            """
            Форматирует дату к читабельному формату

            Arguments:
                date_vac (str): Дата публикации
            returns:
                str: Отформатированная строка даты
            :return:
            """
            date = date_vac[:date_vac.find('T')].split('-')
            return '.'.join(reversed(date))
```  
Результаты :![третийзапуск](https://user-images.githubusercontent.com/97828035/206179803-7585bd6d-945f-44aa-b5bf-0603ed3328e2.jpg)
Метод стал работать значительно быстрее



Также я попыталась усовершенствовать другие методы программы для лучшей производительности:
Изменила метод очистки строки от HTML-кода с этого:
```py
 result = re.sub("<.*?>", '', raw_html)
 return result if '\n' in raw_html else " ".join(result.split())
 ```
 на обычную работу со строкой и ее индексами:
 ```py
  while raw_html.find('<') > -1:
            index1 = raw_html.find('<')
            index2 = raw_html.find('>')
            raw_html = raw_html[:index1] + raw_html[index2 + 1:]
        if '\n' not in raw_html:
            raw_html = " ".join(raw_html.split())
        return raw_html
 ```
 Однако работа метода осталась точно такой же. --->![запускHTML](https://user-images.githubusercontent.com/97828035/206180515-2745f3f9-3817-4c6c-9fe2-302a2d8154fd.jpg)
