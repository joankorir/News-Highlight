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
    #business = get_source('business')
    title = 'Home - Welcome to The News  Website Online'

    return render_template('index.html',title =title, tech_news = tech_news )



@main.route('/source/<id>')
def article(id):
    '''
    View news page function that returns the details page and its data 
    '''
    article =get_article(id)
    title =f'{title}'

    return render_template('news.html', title = title ,article = article)


