# from app import create_app
import urllib.request,json
from .news import Source,Article
api_key = None
# ('b4413de8da704a07811ac7a746c9f70b')
base_url =None
article_url= None
#  app.config['NEWS_API_BASE_URL']

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']
    
    
def get_news(category):
    
    get_news_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
  
    return news_results


def process_results(news_list):
    
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
       
        url = news_item.get('url')
        category = news_item.get('category')
        
        country =news_item.get('country')
        
        source_object = Source(id,name,description,url,category,country)
        news_results.append(source_object)
        
       
        
    return news_results
        
def get_new(title):
    get_news_details_url = base_url.format(title,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
        
        news_object = None
        if news_details_response:
            uid = news_item.response('id')
            name = news_item.response('name')
            author = news_item.response('author')
            title = news_item.response('title')
            description = news_item.response('description')
            url = news_item.response('url')
           
            time = news_item.response('time')
            content = news_item.response('content')
            
            news_object = news(id,name,author,title,description,url,urlToImage,time,content)
    return news_object        


def search_news(news_title):
    search_news_url = 'https://newsapi.org/v2/everything?q=a&apiKey={}'.format(api_key)
    with urllib.request.urlopen(search_news_url)as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)
        
        search_news_results = None
        
        if search_news_results['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(searc_news_list)
        return search_news_results    