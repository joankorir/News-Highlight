import unittest
from .models import source

Source = source.Source


class SourceTest(unittest .Testcase):
    '''
    Test Class to test the behaviour of the Source classs
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(abc-news, ABCNews ,headlines , 'http://abcnews.go.com',general ,english, Us )


    def test_instancee(self):
        self.assertTrue(isinstance(self.source_source,source))

class ArticleTest(unittest.Testcase):
      '''
      Test Class to test the behaviour of the Article class
      '''
      def setUp(self):
          '''
          Set up method that will run before every Test
          '''
          self.new_article = Article(Mark ,Donald Trump scandal ,blah blah staffs, "https://www.youbrandinc.com/crytocurrency/bitcoin-bitcoin-bitcoin-bitcoin-so-sue-us/","https://www.youbrandinc.com/wp-content/uploads/2018/05/Bitcoin-Trademarked-In-The-UK-In-Patent-Troll-Style-Action-1024x538.jpg",The scandal created by Donald ,)

        def test_instance(self):
            self.assertTrue(isinstance(self.new_article ,Article))


if __name__ == '__main__':
    unittest.main()
