import unittest
from firstTask213 import *


class MyTestCase(unittest.TestCase):
    def test_clean_html(self):
        self.assertEqual(DataSet('vacancies.csv').clean_string('<p>Группа компаний «МИАКОМ»</p>'), 'Группа компаний «МИАКОМ»')

    def test_big_count_spaces(self):
        self.assertEqual(DataSet("vacancies.csv").clean_string(f"a      c"), "a c")

    def test_escaped_chars(self):
        self.assertEqual(DataSet("vacancies.csv").clean_string("sdvsd\nascc"), "sdvsd\nascc")

    def test_filter_currency(self):
        vac1=Vacancy({'name':'Аналитик',
                      'description':'Емае',
                      'key_skills':'Нет данных',
                      'experience_id':'noExperience',
                      'premium':'true',
                      'employer_name':'Нет данных',
                      'salary_from':'100',
                      'salary_to':'1000',
                      'salary_gross':'true',
                      'salary_currency':'EUR',
                      'area_name':'Москва',
                      'published_at':'2022-07-06T02:05:26+0300'})
        vac2 = Vacancy({'name': 'Программист',
                        'description': 'Емае',
                        'key_skills': 'Нет данных',
                        'experience_id': 'noExperience',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '500',
                        'salary_to': '2000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vacancies=[vac1,vac2]
        res=[vac2]
        self.assertEqual(InputConect('','','',[0,70],'').data_filter(vacancies,['Идентификатор валюты оклада','Рубли']),res)
    def test_filter_salary(self):
        vac1=Vacancy({'name':'Аналитик',
                      'description':'Емае',
                      'key_skills':'Нет данных',
                      'experience_id':'noExperience',
                      'premium':'true',
                      'employer_name':'Нет данных',
                      'salary_from':'100',
                      'salary_to':'1000',
                      'salary_gross':'true',
                      'salary_currency':'EUR',
                      'area_name':'Москва',
                      'published_at':'2022-07-06T02:05:26+0300'})
        vac2 = Vacancy({'name': 'Программист',
                        'description': 'Емае',
                        'key_skills': 'Нет данных',
                        'experience_id': 'noExperience',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '500',
                        'salary_to': '2000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vacancies=[vac1,vac2]
        res=[vac1,vac2]
        self.assertEqual(InputConect('', '', '', [0, 70], '').data_filter(vacancies, ['Оклад', '900']), res)

    def test_filter_skills(self):
        vac1=Vacancy({'name':'Верстальщик',
                      'description':'Емае',
                      'key_skills':'JS\nHTML5',
                      'experience_id':'noExperience',
                      'premium':'true',
                      'employer_name':'Нет данных',
                      'salary_from':'100',
                      'salary_to':'1000',
                      'salary_gross':'true',
                      'salary_currency':'EUR',
                      'area_name':'Москва',
                      'published_at':'2022-07-06T02:05:26+0300'})
        vac2 = Vacancy({'name': 'Программист',
                        'description': 'Емае',
                        'key_skills': 'Python\nSQL\nFlask',
                        'experience_id': 'noExperience',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '500',
                        'salary_to': '2000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vacancies=[vac1,vac2]
        res=[vac2]
        self.assertEqual(InputConect('', '', '', [0, 70], '').data_filter(vacancies, ['Навыки', 'SQL']), res)

    def test_sort_work_experience(self):
        vac1=Vacancy({'name':'Верстальщик',
                      'description':'Емае',
                      'key_skills':'JS\nHTML5',
                      'experience_id':'noExperience',
                      'premium':'true',
                      'employer_name':'Нет данных',
                      'salary_from':'100',
                      'salary_to':'1000',
                      'salary_gross':'true',
                      'salary_currency':'EUR',
                      'area_name':'Москва',
                      'published_at':'2022-07-06T02:05:26+0300'})
        vac2 = Vacancy({'name': 'Программист',
                        'description': 'Емае',
                        'key_skills': 'Python\nSQL\nFlask',
                        'experience_id': 'between1And3',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '500',
                        'salary_to': '2000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vac3 = Vacancy({'name': 'Аналитик',
                        'description': 'Емае',
                        'key_skills': 'Math\nSQL',
                        'experience_id': 'noExperience',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '500',
                        'salary_to': '2000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vacancies=[vac1,vac2,vac3]
        res=[vac1,vac3,vac2]
        self.assertEqual(InputConect('', '', '', [0, 70], '').data_sort(vacancies, 'Опыт работы',False), res)

    def test_sort_salary_with_different_currency(self):
        vac1=Vacancy({'name':'Верстальщик',
                      'description':'Емае',
                      'key_skills':'JS\nHTML5',
                      'experience_id':'noExperience',
                      'premium':'true',
                      'employer_name':'Нет данных',
                      'salary_from':'100',
                      'salary_to':'1000',
                      'salary_gross':'true',
                      'salary_currency':'EUR',
                      'area_name':'Москва',
                      'published_at':'2022-07-06T02:05:26+0300'})
        vac2 = Vacancy({'name': 'Программист',
                        'description': 'Емае',
                        'key_skills': 'Python\nSQL\nFlask',
                        'experience_id': 'between1And3',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '500',
                        'salary_to': '2000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vac3 = Vacancy({'name': 'Аналитик',
                        'description': 'Емае',
                        'key_skills': 'Math\nSQL',
                        'experience_id': 'noExperience',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '2000',
                        'salary_to': '3000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vacancies=[vac1,vac2,vac3]
        res=[vac1,vac3,vac2]
        self.assertEqual(InputConect('', '', '', [0, 70], '').data_sort(vacancies, 'Оклад',True), res)

    def test_sort_skills(self):
        vac1=Vacancy({'name':'Верстальщик',
                      'description':'Емае',
                      'key_skills':'JS\nHTML5\nGit\nCSS',
                      'experience_id':'noExperience',
                      'premium':'true',
                      'employer_name':'Нет данных',
                      'salary_from':'100',
                      'salary_to':'1000',
                      'salary_gross':'true',
                      'salary_currency':'EUR',
                      'area_name':'Москва',
                      'published_at':'2022-07-06T02:05:26+0300'})
        vac2 = Vacancy({'name': 'Программист',
                        'description': 'Емае',
                        'key_skills': 'Python\nSQL\nFlask',
                        'experience_id': 'between1And3',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '500',
                        'salary_to': '2000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vac3 = Vacancy({'name': 'Аналитик',
                        'description': 'Емае',
                        'key_skills': 'Math\nSQL',
                        'experience_id': 'noExperience',
                        'premium': 'false',
                        'employer_name': 'Нет данных',
                        'salary_from': '2000',
                        'salary_to': '3000',
                        'salary_gross': 'true',
                        'salary_currency': 'RUR',
                        'area_name': 'Екатеринбург',
                        'published_at': '2022-07-06T02:05:26+0300'})
        vacancies=[vac1,vac2,vac3]
        res=[vac1,vac2,vac3]
        self.assertEqual(InputConect('', '', '', [0, 70], '').data_sort(vacancies, 'Навыки', True), res)

    def test_formatter(self):
        vac1 = Vacancy({'name': 'Верстальщик',
                        'description': 'Емае',
                        'key_skills': 'JS\nHTML5\nGit\nCSS',
                        'experience_id': 'noExperience',
                        'premium': 'True',
                        'employer_name': 'Нет данных',
                        'salary_from': '1000',
                        'salary_to': '2000',
                        'salary_gross': 'True',
                        'salary_currency': 'EUR',
                        'area_name': 'Москва',
                        'published_at': '2022-07-06T02:05:26+0300'})
        res=['Верстальщик','Емае','JS\nHTML5\nGit\nCSS','Нет опыта','Да','Нет данных',
             '1 000 - 2 000 (Евро) (Без вычета налогов)','Москва','06.07.2022']
        self.assertEqual(InputConect('', '', '', [0, 70], '').formatter(vac1), res)

    def test_formatter_salary(self):
        vac1 = Vacancy({'name': 'Верстальщик',
                        'description': 'Емае',
                        'key_skills': 'JS\nHTML5\nGit\nCSS',
                        'experience_id': 'noExperience',
                        'premium': 'True',
                        'employer_name': 'Нет данных',
                        'salary_from': '1000',
                        'salary_to': '2000',
                        'salary_gross': 'True',
                        'salary_currency': 'EUR',
                        'area_name': 'Москва',
                        'published_at': '2022-07-06T02:05:26+0300'})
        res=['Верстальщик','Емае','JS\nHTML5\nGit\nCSS','Нет опыта','Да','Нет данных',
             '1 000 - 2 000 (Евро) (Без вычета налогов)','Москва','06.07.2022']
        self.assertEqual(InputConect('', '', '', [0, 70], '').formatter(vac1), res)

    def test_formatter_salary(self):
        vac1 = Vacancy({'name': 'Верстальщик',
                        'description': 'Емае',
                        'key_skills': 'JS\nHTML5\nGit\nCSS',
                        'experience_id': 'noExperience',
                        'premium': 'False',
                        'employer_name': 'Нет данных',
                        'salary_from': '300',
                        'salary_to': '900',
                        'salary_gross': 'False',
                        'salary_currency': 'USD',
                        'area_name': 'Москва',
                        'published_at': '2022-12-01T02:05:26+0300'})
        res = ['Верстальщик', 'Емае', 'JS\nHTML5\nGit\nCSS', 'Нет опыта', 'Нет', 'Нет данных',
               '300 - 900 (Доллары) (С вычетом налогов)', 'Москва', '01.12.2022']
        self.assertEqual(InputConect('', '', '', [0, 70], '').formatter(vac1), res)


if __name__ == '__main__':
    unittest.main()
