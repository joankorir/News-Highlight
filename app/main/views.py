from flask import render_template ,request,redirect, url_for
from . import main
from .. request import get_source ,get_news , get_article ,get_everything,search_article

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #Getting breaking news
    breaking_news = get_source('breaking-news')
    title = 'Home - Welcome to The News  Website Online'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
    
         return render_template('index.html',title =title, breaking = breaking_news )



@main.route('/source/<id>')
def article(id):
    '''
    View news page function that returns the details page and its data 
    '''
    article =get_article(id)
    title =f'{news.title}'

    return render_template('news.html', title = title ,article = article)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',articles = searched_articles)
   