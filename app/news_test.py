import unittest 
from .models import news
News = news.News


class NewsTest(unittest.Testcase):
    '''
    Test Class to test the behaviour of the News classs
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test 
        '''
        self.new_news = News(1234 ,'Corruption has been the country fear','The wildfire news','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993))