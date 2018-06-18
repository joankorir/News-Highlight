from flask import render_template ,request,redirect, url_for
from app import app
from .request import get_news ,get_newsHighlight, search_newsHighlight


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

    search_newsHighlight = request.args.get('newsHighlight_query')

    if search_newsHighlight:
        return redirect(url_for('search',newsHighlight_name=search_newsHighlight))
    else:
    return render_template('index.html',title =title,popular=popular_news ,upcoming = upcoming_news , now_showing = now_showing_news)



@app.route('/newshighlight/<int:news_id>')
def newshighlight(id):


    '''
    View newshighlight page function that returns the news details page and its data
    '''

    newshighlight = get_news(id)
    title = f'{newshighlight.title}'
    return render_template('news.html',title = title, newshighlight = newshighlight)


@app.route('/search/<newsHighlight_name>')
def search(newsHighlight_name):
    '''
    View function to display the search results
    '''
    newsHighlight_name_list = newsHighlight_name.split(" ")
    newsHighlight_name_format = "+".join(newsHighlight_name_list)
    searched_news = search_newsHighlight(newsHighlight_name_format)
    title = f'search results for {newsHighlight_name}'
    return render_template('search.html',news = searched_news)


