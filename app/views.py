from flask import render_template
from app import app
from request import get_news


#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The News Highlight Website Online'
    return render_template('index.html',title =title)



@app.route('/newshighlight/<int:news_id>')
def newshighlight(news_id):


    '''
    View newshighlight page function that returns the news details page and its data
    '''
    return render_template('news.html',id =news_id)


