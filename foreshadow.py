#!/usr/bin/env python3
from bs4 import BeautifulSoup
from termcolor import colored, cprint
import requests
import os
import subprocess

if os.path.isfile('config.py'):
    from config import SETTINGS
else:
    print("""couldn't load your config settings. default configs're preferred.""")
    from default_config import SETTINGS

MY_HEADERS = SETTINGS['headers']
if SETTINGS['source'] == 'homepage': R = requests.get(url=SETTINGS['url_homepage'], headers=MY_HEADERS)
elif SETTINGS['source'] == 'archive': R = requests.get(url=SETTINGS['url_archive'], headers=MY_HEADERS)
SOUP = BeautifulSoup(R.content, SETTINGS['parser'])

PRINT_BOLD = lambda x: cprint(x, attrs={'bold'})
PRINT_BOLD_RED = lambda x: cprint(x, 'red', attrs={'bold'})
PRINT_BOLD_GREEN = lambda x: cprint(x, 'green', attrs={'bold'})

def show_news_homepage():
    news = SOUP.find('div', attrs={'id': 'news'})
    news_len = len(news.find_all('h4'))
    news_titles = news.find_all('h4')
    news_timestamps = news.find_all('p', attrs={'class': 'timestamp'})
    news_article_contents = news.find_all('div', attrs={'class': 'article-content'})

    if SETTINGS['bottom_up']:
        news_titles.reverse()
        news_timestamps.reverse()
        news_article_contents.reverse()

    for new_loop in range(news_len):
        news_title = news_titles[new_loop].find('a').text
        news_timestamp = news_timestamps[new_loop].text
        news_article_content = news_article_contents[new_loop]

        output_text = colored('[' + news_timestamp + '] ' + news_title, 'white', attrs={'bold'})
        print(output_text)
        for _ in range(len(output_text)):
            print(colored('=', 'white', attrs={'bold'}), end='')
        print('')

        for article in news_article_content.find('p'):
            print(article, end='')

        print('\n')

def show_news_archive():
    news = SOUP.find('table', attrs={'id': 'article-list', 'class': 'results'}).find('tbody').find_all('tr')
    news_len = len(news)

    if SETTINGS['bottom_up']: news.reverse()
    
    for new_loop in range(news_len):
        selected_news = news[new_loop]
        selected_news_title = selected_news.find_all('td')[1].find('a').text
        selected_news_published_date = selected_news.find_all('td')[0].text
        selected_news_author = selected_news.find_all('td')[2].text
        output_text = colored('[{}]'.format(selected_news_published_date), 'white', attrs={'bold'}) + ' {} - {}'.format(selected_news_title, selected_news_author) 
        print(output_text)
        for _ in range(len(output_text)): print(colored('', 'white', attrs={'bold'}), end='')
        print('')

def ask_update():
    try:
        get_answer = input(colored('::', 'blue', attrs={'bold'}) + ' ' + colored('Do you want to update your system right now? [y/N]: ', 'white', attrs={'bold'}))
        if get_answer.lower() == 'y': result_process = subprocess.run(['sudo', 'pacman', '-Syu'])
        else: PRINT_BOLD_RED('Cancelled.')
    except KeyboardInterrupt: PRINT_BOLD_RED('Keyboard Interrupt.')

if __name__ == '__main__':
    result_process = subprocess.run(['clear'])
    if SETTINGS['source'] == 'homepage': show_news_homepage()
    elif SETTINGS['source'] == 'archive': show_news_archive()
    ask_update()
