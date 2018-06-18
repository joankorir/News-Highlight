from flask import render_template
from app import app
from .request import get_news ,get_newsHighlight


#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #Getting popular news 
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news = get_news('now_trending')
    title = 'Home - Welcome to The News Highlight Website Online'
    return render_template('index.html',title =title,popular=popular_news ,upcoming = upcoming_news , now_showing = now_showing_news)



@app.route('/newshighlight/<int:news_id>')
def newshighlight(id):


    '''
    View newshighlight page function that returns the news details page and its data
    '''

    newshighlight = get_news(id)
    title = f'{newshighlight.title}'
    return render_template('news.html',title = title, newshighlight)


