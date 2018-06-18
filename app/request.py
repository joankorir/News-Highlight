from app import app
import urllib.request,json
from .models import news


News = news.News

#Getting api key 
api_key = app.config['NEWS_API_KEY']

#Getting the news base url 
base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)


    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None


        if get_news_response['results']:
            news_results_list = get_news_response['results']

            news_results = process_results(news_results_list)





        return news_results


    def process_results(news_list):
        '''
        Function that processes the news result and transform them to a list of objects
    

        Args:
            news_list:A list of dictionaries that contain news details

        Returns:
            news_results:A list of news objects
        '''
        news_results = []
        for news_item in news_list:
            id = news_item.get('id')
            title = news_item.get('original_title')
            overview = news_item.get('overview')
            poster = news_item.get('poster_path')
            timeCreated = news_item.get('timeCreated')

            if poster:
                news_object = News(id,title,overview,poster,timeCreated)
                news_results.append(news_object)
    
    
        return news_results 

    def get_newsHighlight(id):
      get_newsHighlight_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_newsHighlight_details_url) as url:
        newsHighlight_details_data = url.read()
        newsHighlight_details_response = json.loads(newsHighlight_details_data)

        newsHighlight_object = None
        if newsHighlight_details_response:
            id = newsHighlight_details_response.get('id')
            title = newsHighlight_details_response.get('original_title')
            overview = newsHighlight_details_response.get('overview')
            poster = newsHighlight_details_response.get('poster_path')
            timeCreated = newsHighlight_details_response.get('timeCreated')

            newsHighlight_object = NewsHighlight(id,title,overview,poster,timeCreated)

    return newsHighlight_object


    def search_newsHighlight(newsHighlight_name):
    search_newsHighlight_url = 'https://api.thenewsb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_newsHighlight_url) as url:
        search_newsHighlight_data = url.read()
        search_newsHighlight_response = json.loads(search_newsHighlight_data)

        search_newsHighlight_results = None

        if search_newsHighlight_response['results']:
            search_newshighlight_list = search_newsHighlight_response['results']
            search_newsHighlight_results = process_results(search_movie_list)


    return search_movie_results




    




        
