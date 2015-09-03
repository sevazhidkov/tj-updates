# TJ Updates
Скрипт, который присылает последние новости TJournal и лучшие твиты прямо в ВКонтакте (поддержка Telegram планируется)
### Установка
```
pip install requests vk_api feedparser pyquery
git clone https://github.com/Shamoi/tj-updates.git
cd tj-updates
python config.py
```
Настройте send_to.json:
```
[
    {
        "id": 91670994,
        "type": "vk",
        "press": "russian_it",
        "name": "Сева",
        "hour": 9
    },
    {
        "id": 1,
        "type": "vk",
        "press": "belarusian",
        "name": "Паша",
        "hour": 9
    },
]
```
id - идентификатор пользователя в нужном сервисе(vk/telegram)

type - "vk" или "telegram" (пока не работает)

press - нужная тема для анализа СМИ, например, russian - российская пресса, russian_it - русские IT-издание, english - западные СМИ, english_it - западные IT-издания, ukrainian - украинские СМИ, belarusian - белорусские СМИ.

name - скрипт будет называть пользователя этим именем, например, "Паша", "Сева", "Сволочьвернидолг"

hour - час, в который нужно присылать сообщение. Убедитесь, что cron запускает скрипт только один раз за этот час.
### Запуск
```
python parse_news.py
```
Если вы хотите настроить автоматический запуск, сделайте это с помощью cron:
```
sudo crontab -e
0 9 * * *  cd ~/tj-updates && python parse_news.py # Запускать скрипт каждый день в 9:00
0 18 * * *  cd ~/tj-updates && python parse_news.py # Запускать скрипт каждый день в 18:00
```
Необходимо указывать все те часы, когда вы хотите, чтобы скрипт запустился. Все часы должны быть указаны в send_to.json

Для поддержки Telegram необходимо установить модуль pytg (https://github.com/luckydonald/pytg) и запустить telegram-cli:
```bash
bin/telegram-cli --json -P 4458
```
### Контакты
Если вы хотите получать такие сообщения, но не хотите настраивать скрипт - напишите мне в ВКонтакте: https://vk.com/shamoiseva
### TODO
1. Добавить поддержку Telegram

2. Прикладывать фотографии из твитов к сообщению
