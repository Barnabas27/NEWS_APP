from flask import render_template,request,redirect,url_for
from . import main

from ..request import get_news, get_new,search_news

@main.route('/')
def index():
    
    popular_news = get_news('general')
    entertainment_news = get_news('entertainment')
    technology_news = get_news('technology')
    business_news = get_news('business')
    health_news = get_news('health')
    science_news=get_news('science')
    sports_news=get_news('sports')
   
    title = 'Home - Here is news for you'
    
   
   
    return render_template('index.html', title = title, general = popular_news, entertainment = entertainment_news, technology = technology_news, business = business_news, health = health_news, science = science_news, sports = sports_news)
   
        
        
    

@main.route('/sources/<news_id>')
def news(news_id):
    news = get_new(id)
    title = f'{news.title}'
    return render_template('article.html',title = title, news = news)


@main.route('/search/<news_title>')
def search(news_title):
    
    news_title_list = news_title.split(" ")
    news_title_format = "+".join(news_title_list)
    searched_news = search_news(news_title_format)
    title = f'search results for {news_title}'
    return render_template('search.html',news = searched_news)