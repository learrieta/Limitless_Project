from django.shortcuts import render
from .models import Article, Comment
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})




