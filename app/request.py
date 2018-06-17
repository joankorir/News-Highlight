from app import app
import urllib.request,json
from .models import news


News = news.News

#Getting api key 
api_key = app.config['News_API_KEY']

#Getting the news base url 
base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)


    with urllib.request.urlopen(get_movies_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        