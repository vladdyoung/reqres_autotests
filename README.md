# Автотесты API
## Описание проекта
1. Предусмотрена возможность запуска тестов в разных браузерах (Chrome, Firefox). В том числе есть возможность
запуска тестов на удаленной платформе с помощью Selenoid.
2. В целях предотвращения проверки на бота сайтом yandex.ru использованы опции добавления User_Agent.
3. Для логирования использована стандартная библиотека logging.
4. В целях демонстрации различных методов проверок используется стандартный метод assert, а также конструкция try/except.
5. Используются явные и неявные ожидания элементов страницы.
6. Для формирования отчетов используется библиотека Allure.
7. Предусмотрен запуск тестов в полноэкранном режиме браузера.
8. Предусмотрена возможность запуска тестов в headless режиме.

## Запуск тестов
### Аргументы командной строки для запуска тестов:

+ Локальный запуск браузера с установленным драйвером: 
  + --browser_name=chrome/firefox(default=chrome)
```commandline
pytest --browser_name=firefox tests
```
+ Удаленный запуск браузера c использованием Selenoid (перед запуском необходимо скачать docker image selenoid):
  + --browser_name=remote
  + --browser_name_remote=chrome/firefox/opera(default=chrome)
  + --version_remote_browser=(default=102.0)
  + --vnc=(default=True) Для записи видео прохождения теста
  + --executor=(default-localhost) IP Selenoid.
```commandline
pytest --browser_name=remote --browser_name_remote=chrome --version_remote_browser=102.0 --vnc=True --executor=localhost tests
```
+ Запуск в headless режиме: --headless=true/false(default=true)
```commandline
pytest --headless=true tests
```

### Формирование отчетов о прохождении тестов:
Находясь в корне проекта, в командной строке вести команду:
```commandline
allure sesve
```




