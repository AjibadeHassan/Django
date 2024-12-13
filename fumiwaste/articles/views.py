from django.shortcuts import render


# Create your views here.
def article_list(req):
    return render(req, 'articles/article_list.html')