# Автотесты API web-ресурса reqres.ini
## Описание проекта
1. Предусмотрена возможность запуска тестов в разных браузерах (Chrome, Firefox). В том числе есть возможность
запуска тестов на удаленной платформе с помощью Selenoid.
2. В целях предотвращения проверки на бота использованы опции добавления User_Agent.
3. Для логирования использована стандартная библиотека logging.
4. В целях демонстрации различных методов проверок используется стандартный метод assert, а также конструкция try/except.
5. Используются явные и неявные ожидания элементов страницы.
6. Для формирования отчетов используется библиотека Allure.
7. Предусмотрен запуск тестов в полноэкранном режиме браузера.
8. Предусмотрена возможность запуска тестов в headless режиме.
9. Предусмотрена возможность запуска тестов с помощью Docker.
10. В целях демонстрации к проекту прикреплены скриншоты запуска тестов с помощью Jenkins.

## Запуск тестов
### Аргументы командной строки для запуска тестов:

+ Локальный запуск браузера с установленным драйвером: 
  + --browser_name=chrome/firefox
```commandline
pytest --browser_name=firefox tests
```
+ Удаленный запуск браузера c использованием Selenoid (перед запуском необходимо скачать docker image selenoid):
  + --browser_name=remote(default=remote)
  + --browser_name_remote=chrome/firefox/opera(default=chrome)
  + --version_remote_browser=(default=103.0) Следите за доступными версиями браузеров в Selenoid UI.
  + --vnc=(default=False) для записи видео прохождения теста
  + --executor=(default=localhost) IP Selenoid.

######!!!Внимание!!! Для запуска тестов с помощью Selenoid в параметр --executor следует передать IP-адрес беспроводного сетевого соединения Вашего компьютера.
Например: --executor=192.168.0.190

```commandline
pytest --browser_name=remote --browser_name_remote=chrome --version_remote_browser=103.0 --vnc=True --executor=192.168.0.190 tests
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
### Запуск тестов с помощью Docker и формирование отчетов Allure:
Для запуска тестов с помощью Docker необходимо клонировать данный репозиторий в локальное хранилище и выполнить следующе команды:
```commandline 
docker run --name tests_run --network selenoid tests pytest --browser_name=remote
docker cp tests_run:/app/allure-results .
allure serve
```




