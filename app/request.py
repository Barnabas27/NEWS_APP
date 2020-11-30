from app import app
import urllib.request,json
from .models import news

api_key = ('b4413de8da704a07811ac7a746c9f70b')
base_url = app.config['NEWS_API_BASE_URL']

def get_news(articles):
    get_news_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
            
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
    # print(get_news_url)
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
    # print(get_news_data)
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
    # print(news_results_list)
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
    # print(news_results)
    # print('vvvvvvvvvvvvvvvvvvvvvvv')
            
            
    return news_results_list


def process_results(news_list):
    
    news_results = []
    for news_item in news_list:
        uid = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage =news_item.get('urlToImage')
        time = news_item.get('time')
        content = news_item.get('content')
        
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
            # urlToImage =news_item.response('urlToImage')
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