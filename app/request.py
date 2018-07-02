# from app import app
import urllib.request,json
from .models import Source ,Article


# Source = source.Source
Article = Article

#Getting api key
api_key = None

#Getting the news base url
base_url = None
article_base_url = None


def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    print(get_source_url)


    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        # print(get_source_data)
        get_source_response = json.loads(get_source_data)
        # print (get_source_response)
        source_results = None


        if get_source_response['sources']:
            source_results_list = get_source_response['sources']


            source_results = process_results(source_results_list)
        return source_results


def process_results(source_list):
    '''
    Function that processes the news result and transform them to a list of objects


    Args:
        source_list:A list of dictionaries that contain source details

    Returns:
        source_results:A list of source objects
    '''
    source_results = []
    for source_item in source_list:

        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')


        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results

# def get_news(id):
#     get_news_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(news_details_data)

#         news_object = None
#         if news_details_response:
#             id = news_details_response.get('id')
#             name = news_details_response.get('name')
#             description = news_details_response.get('description')
#             url = news_details_response.get('url')
#             category = news_details_response.get('category')
#             language= news_details_response.get('language')
#             country = news_details_response.get('country')

#             news_object = Source(id,name,description,url,category,language,country)

#     return news_object


def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_base_url.format(id,api_key)


    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None


        if get_article_response['articles']:
            article_results_list = get_article_response['articles']

            article_results = process_results(article_results_list)
    return article_results

def process_article(article_list):
    '''
    Function that processes the news result and transform them to a list of objects


    Args:
        Article_list:A list of dictionaries that contain Article details

    Returns:
        article_results:A list of article objects
    '''
    article_results = []
    for article_item in article_list:
      author = article_item.get('author')
      title = article_item.get('title')
      description = article_item.get('description')
      url = article_item.get('url')
      urlToImage = article_item.get('urlToImage')
      publishedAt = article_item.get('country')

      if urlToImage:
            article_object = Article(author,title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)

    return article_results



def get_everything(id):
    get_everything_details_url = article_base_url.format(id,api_key)

    with urllib.request.urlopen(get_everything_details_url) as url:
        everything_details_data = url.read()
        everything_details_response = json.loads(everything_details_data)

        everything_object = None
        if everything_details_response:
            # id = everything_details.get('id')
            author = everything_details_response.get('author')
            title = everything_details_response.get('title')
            description = everything_details_response.get('description')
            url = everything_details_response.get('url')
            urlToImage= everything_details_response.get('urlToImage')
            publishedAt = everything_details_response.get('publishedAt')

            everything_object = Article(author,title,description,url,urlToImage,publishedAt)

    return everything_object
