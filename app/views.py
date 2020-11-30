from flask import render_template,request,redirect,url_for
from app import app
# from request import get_news,get_new
from .request import get_news, get_new,search_news

@app.route('/')
def index():
    
    popular_news = get_news('popular')
    # print(popular_news)
    title = 'Home - Here is news for you'
    
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_title=search_news))
    else:
        
        return render_template('index.html',title = title, popular = popular_news)
    

@app.route('/news/<news_id>')
def news(news_id):
    news = get_new(id)
    title = f'{news.title}'
    return render_template('news.html',title = title, news = news)


@app.route('/search/<news_title>')
def search(news_title):
    
    news_title_list = news_title.split(" ")
    news_title_format = "+".join(news_title_list)
    searched_news = search_news(news_title_format)
    title = f'search results for {news_title}'
    return render_template('search.html',news = searched_news)