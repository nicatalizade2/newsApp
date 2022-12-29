from django.shortcuts import render
import requests, random
# from newsapi import NewsApiClient


def index(request):
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8b92e3d1a18c42c4969cbb334edbf2de').json()
    articles = r['articles']
    # random_item = random.randint(0, len(articles)-1)
    return render(request, 'news/index.html', {
        'news': articles
    })

def newsAll(request):
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8b92e3d1a18c42c4969cbb334edbf2de').json()
    articles = r['articles']
    return render(request, 'news/news_all.html', {
        'news': articles
    })


