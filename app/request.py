from app import app
import urllib.request,json
from .models import news

api_key = app.config['NEWS_API_KEY ']
base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    get_news_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['response']:
            news_results_list = get_news_response['response']
            news_results = process_results(news_results_list)
            
            
    return news_results


def process_results(news_list):
    
    news_results = []
    for news_item in news_list:
        uid = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urltoimage =news_item.get('urltoimage')
        time = news_item.get('time')
        content = news_item.get('content')
