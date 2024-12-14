from django.shortcuts import render
from .models import Article


# Create your views here.
def article_list(req):
    articles = Article.objects.all().order_by('date')
    return render(req, 'articles/article_list.html', {'articles': articles})