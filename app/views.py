from flask import render_template
from app import app
from request import get_news

@app.route('/')
def index():
    
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Here is news for you'
    return render_template('index.html',title = title, popular = popular_news)
    


# @app.route('/news/<news_id>')
# def news(news_id):
#     return render_template('news.html',id = news_id)