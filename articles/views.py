from django.shortcuts import render
from .models import Article
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def article_list(request):
    articles = Article.objects.all().order_by("date")
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        articles = paginator.page(paginator.num_pages)
    return render(request,
                  'articles/article_list.html',
                  {'page': page,
                   'articles': articles})

def tag_view(request, tag):
    articles = Article.objects.filter(tags__name__in = [str(tag)])
    print(articles)
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        articles = paginator.page(paginator.num_pages)
    return render(request,
                  'articles/tags_list.html',
                  {'page': page,
                   'articles': articles})





def article_details(request, slug):

    article = Article.objects.get(slug=slug)
    tags = article.tags.all()
    related_articles = Article.simiar(article)

    return render(request,'articles/article_detail.html', {'article': article, 'tags': tags, 'related_articles': related_articles})