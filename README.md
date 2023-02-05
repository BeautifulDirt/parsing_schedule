# Парсинг расписания с сайта телевизионного канала и верстка картинки для поста и сториз в соцсетях

:star: STAR ME!

 <img src="./src/readme/5tv_schedule.jpg" width="640">

Я администратор [ВК-группы](https://vk.com/serial_sled "Ссылка на ВК-группу") и [Telegram-канала](https://t.me/serial_sled_official "Ссылка на tg-канал"), которые посвящены популярному детективному сериалу "След". Туда мы публикуем посты с анонсами, различные медиа, интервью и расписания показа сериала по выходным на Пятом канале. Количество серий, транслирующихся в день, в среднем больше пяти. Это расписание имеет свойство меняться за день телепоказа, поэтому чтобы судорожно не менять вручную сторизы и посты для соцсетей и не проверять каждый раз их актуальность сформированных нами ранее, была необходимость написать бота, который парсит телепрограмму с [телевизионного сайта](https://www.5-tv.ru/schedule/ "Ссылка на телепрограмму Пятого канала") *(если меня читают работники телеканала, не переживайте, мой бот не представляет угрозу вашему сайту, это равносильно пользователю, который за день решил уточнить для себя расписание телепередач)*, находит все серии по наименованию, уведомляет нас и парсит сториз для ВК и ТГ, затем на следующее утро их туда публикует.   

 ### Инструкция для запуска

Создаем образ для будущих контейнеров, на основе которых будут запускаться **python-скрипты** по **cron**:

`docker build -t dirt_py_cron:3.8-slim-buster .`

Клонируем себе **git-репозиторий**, переходим в папку с проектом и запускаем развертывание **docker-конейнера** в фоновом режиме: 

`docker-compose up -d`

Чтобы узнать успешно ли собрался контейнер необходимо подать команду:

`docker-compose logs sled_schedule`

Если **cron** был запущен, то контейнер был успешно поднят:

```sh
...
sled_schedule    | Starting periodic command scheduler: cron.
```

Для остановки и последующего удаления контейнера используйте:

`docker-compose down`


:calendar: сентябрь, 2022 год