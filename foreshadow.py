#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import os

if os.path.isfile('config.py'):
    from config import SETTINGS
else:
    print("""couldn't load your config settings. default configs're preferred.""")
    from default_config import SETTINGS

MY_HEADERS = SETTINGS['headers']
R = requests.get(url=SETTINGS['url'], headers=MY_HEADERS)
SOUP = BeautifulSoup(R.content, SETTINGS['parser'])

def show_news():
    news = SOUP.find('div', attrs={'id': 'news'})
    news_len = len(news.find_all('h4'))
    news_titles = news.find_all('h4')
    news_timestamps = news.find_all('p', attrs={'class': 'timestamp'})
    news_article_contents = news.find_all('div', attrs={'class': 'article-content'})

    for new_loop in range(news_len):
        news_title = news_titles[new_loop].find('a').text
        news_timestamp = news_timestamps[new_loop].text
        news_article_content = news_article_contents[new_loop]

        print('[ ' + news_timestamp + ' ] ' + news_title)
        for _ in range(len('[ ' + news_timestamp + ' ] ' + news_title)):
            print('=', end='')
        print('')

        for article in news_article_content.find('p'):
            print(article, end='')

        print('\n')

if __name__ == '__main__': show_news()
