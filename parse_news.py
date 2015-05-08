import feedparser
import json
from send_message import send_vk_message, send_telegram_message

subscribers = json.loads(open('send_to.json').read())


def get_5_latest_news():
    latest_news = ['Последние новости:']
    news = feedparser.parse('http://tjournal.ru/rss')['items']
    # Get 5 news
    for i in range(5):
        latest_news.append('{title} - {link}'.format(
            title=news[i]['title'],
            link=news[i]['link']
        ))
    return latest_news


def get_3_best_tweets():
    return ['Последние твиты:']

digest = get_5_latest_news() + get_3_best_tweets()
for subscriber in subscribers:
    if subscriber['type'] == 'vk':
        send_vk_message(digest, subscriber['id'])
    else:
        send_telegram_message(digest, subscriber['id'])


