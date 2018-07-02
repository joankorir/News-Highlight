from flask import render_template ,request,redirect, url_for
from . import main
from .. request import get_source , get_article

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #Getting breaking news
    tech_news = get_source('technology')
    health_news = get_source('health')
    enter_news = get_source('Entertainment')
    business_news = get_source('business')
    sports_news = get_source('sports')

    #business = get_source('business')
    title = 'Home - Welcome to The News  Website Online'

    return render_template('index.html',title =title ,tech_news =tech_news ,health_news =health_news ,enter_news =enter_news,business_news =business_news ,sports_news =sports_news )



@main.route('/source/<id>')
def article(id):
    '''
    View news page function that returns the details page and its data
    '''
    article = get_article(id)
    print(article)
    title =f'{id}'

    return render_template('news.html', title = title ,article = article)
