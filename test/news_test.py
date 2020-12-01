import unittest
from models import news

News = news.News

class NewsTest(unittest.TestCase):
    
    def setUp(self):
        
        self.new_news = News('Timothy B. Lee Ars Technica','An Engineer Gets 9 Years for Stealing $10M From Microsoft','The defendant tried—and failed—to use bitcoin to cover his tracks.','https://www.wired.com/story/an-engineer-gets-9-years-for-stealing-dollar10m-from-microsoft/','https://media.wired.com/photos/5fac6afb446b4639b3d5b8d8/191:100/w_1280,c_limit/Security-Microsoft-1229426260.jpg','2020-11-12T14:00:00Z','A former Microsoft software engineer from Ukraine has been sentenced to nine years in prison for stealing more than $10 million in store credit from Microsoft\'s online store. From 2016 to 2018, Volod… [+3307 chars]')
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        
if __name__ == '__main__':
    unittest.main()