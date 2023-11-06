Issue_5

В этой папке протестирована функция what_is_year_now() с помощью unittest.mock, pytest и pytest-cov.

Шаги для запуска:

1)Зайти в папку issue_5

2)Запустить файл test_issue_5.py, используя команду python3 -m pytest -v 


3) Для получения замеров покрытия нужно запусить файл test_issue_5.py, используя команду python3 -m pytest -q --cov . --cov

4)Для выгрузки отчета о замерах покрытия в html нужно запусить файл test_issue_5.py, используя команду python3 -m pytest --cov . --cov-report html
