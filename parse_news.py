import feedparser
import json
import requests
from pyquery import PyQuery
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
    best_tweets = ['Лучшие твиты:']
    # HTML query in jQuery style to get best tweets
    html_query = '.container .b-content .b-content-wrapper ' + \
                 '.b-content__b1 .b-block .b-articles ' + \
                 '.b-articles__b'
    tj_tweets_page = requests.get('http://tjournal.ru/tweets').text
    tweets_html = PyQuery(tj_tweets_page)
    for i in range(3):
        html_tweet_query = html_query + ':eq( {} )'.format(str(i))
        tweet_html = tweets_html(html_tweet_query)
        tweet_text = tweet_html('.b-articles__b__text').text()
        tweet_author = tweet_html('.b-articles__b__name').text()
        #TODO: Attach tweet photo to message attachments
        if tweet_html('.b-articles__b__picture'):
            tweet_picture_html = tweet_html('.b-articles__b__picture a')
            tweet_picture = tweet_picture_html.attr('href')
        else:
            tweet_picture = None
        best_tweets.append('{author}: "{tweet}"<br>{picture}'.format(
            author=tweet_author,
            tweet=tweet_text,
            picture=tweet_picture if tweet_picture is not None else ''
        ))
    return best_tweets

digest = get_5_latest_news() + get_3_best_tweets()
for subscriber in subscribers:
    if subscriber['type'] == 'vk':
        send_vk_message(digest, subscriber['id'])
    else:
        send_telegram_message(digest, subscriber['id'])


