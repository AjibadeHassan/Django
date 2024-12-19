from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def article_list(req):
    articles = Article.objects.all().order_by('date')
    return render(req, 'articles/article_list.html', {'articles': articles})


def article_details(req,slug):
    print({slug})
    # return HttpResponse( {slug})
    article = Article.objects.get(slug=slug)
    return render(req,'articles/article_detail.html', {'article': article})
@login_required(login_url='/accounts/login/')
def article_create(req):
    return render(req, 'articles/article_create.html')