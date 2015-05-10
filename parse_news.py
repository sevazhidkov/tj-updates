import feedparser
import json
import requests
from datetime import datetime
from pyquery import PyQuery
from send_message import send_vk_message, send_telegram_message

subscribers = json.loads(open('send_to.json').read())


def get_3_latest_news():
    latest_news = ['Последние новости:']
    news = feedparser.parse('http://tjournal.ru/rss')['items']
    # Get 3 news
    for i in range(3):
        latest_news.append('{title} - {link}'.format(
            title=news[i]['title'],
            link=news[i]['link']
        ))
    return latest_news


def get_media_analyze(press_type):
    media_news = ['Анализ СМИ:']
    get_block_query = '.container .b-content .b-block #blockNews{}'
    get_article_query = '.b-index-news .b-index-news__b:eq( {} )'
    # Select num, which contains in DOM.
    # For example, "#blockNews2" is the
    # block with russian news
    if press_type == 'russian':
        press_num = 2
    elif press_type == 'russian_it':
        press_num = 1
    elif press_type == 'english_it':
        press_num = 3
    elif press_type == 'ukrainian':
        press_num = 5
    elif press_type == 'belarusian':
        press_num = 7
    else:
        print('Unsupporting press type')
        return []
    news_html = PyQuery(requests.get('http://tjournal.ru/news').text)
    news_block_html = news_html(get_block_query.format(str(press_num)))
    # Get 3 articles
    for i in range(3):
        article_html = news_block_html(get_article_query.format(str(i)))
        # Article title contains in the link with tag <b>
        article_title = article_html('a b').text()
        # Article source contains in 'alt' attribute of image
        article_source = article_html('a img').attr('alt')
        article_link = article_html('a').attr('href')
        media_news.append('{source}: {title} - {link}'.format(
            source=article_source,
            title=article_title,
            link=article_link
        ))
    return media_news


def get_3_best_tweets():
    best_tweets = ['Лучшие твиты:']
    # HTML query in jQuery style to get best tweets
    html_query = '.container .b-content .b-content-wrapper ' + \
                 '.b-content__b1 .b-block .b-articles ' + \
                 '.b-articles__b'
    tj_tweets_page = requests.get('http://tjournal.ru/tweets').text
    tweets_html = PyQuery(tj_tweets_page)
    # Get 3 tweets
    for i in range(3):
        html_tweet_query = html_query + ':eq( {} )'.format(str(i))
        tweet_html = tweets_html(html_tweet_query)
        tweet_text = tweet_html('.b-articles__b__text').text()
        tweet_author = tweet_html('.b-articles__b__name').text()
        #TODO: Attach tweet photo to message attachments
        best_tweets.append('{author}: "{tweet}"'.format(
            author=tweet_author,
            tweet=tweet_text
        ))
    return best_tweets

digest = get_3_latest_news() + get_3_best_tweets()
for subscriber in subscribers:
    # Check, that subscriber want to
    # receive messages in this hour
    now_hour = datetime.timetuple(datetime.now())[3]
    if subscriber['hour'] != now_hour:
        continue
    digest += get_media_analyze(subscriber['press'])
    if subscriber['type'] == 'vk':
        send_vk_message(digest, subscriber['id'], subscriber['name'])
    else:
        send_telegram_message(digest, subscriber['id'], subscriber['name'])


