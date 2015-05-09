# TJ Updates
Скрипт, который присылает последние новости TJournal и лучшие твиты прямо в ВКонтакте (поддержка Telegram планируется)
### Установка
```

git clone https://github.com/Shamoi/tj-updates.git
cd tj-updates
python config.py
```
Настройте send_to.json:
```
[
    {
        "id": 91670994,
        "type": "vk"
    },
    {
        "id": 1,
        "type": "vk"
    }
]
```
### Запуск
```
python parse_news.py
```
Если вы хотите настроить автоматический запуск, сделайте это с помощью cron:
```
sudo crontab -e
* 9 * * *  cd ~/tj-updates && python parse_news.py # Запускать скрипт каждый день в 9:00
```
### Контакты
Если вы хотите получать такие сообщения, но не хотите настраивать скрипт - напишите мне в ВКонтакте: https://vk.com/shamoiseva
### TODO
1. Добавить поддержку Telegram

2. Прикладывать фотографии из твитов к сообщению
