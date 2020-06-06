from django.shortcuts import render
from .models import Article, Category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag



def article_list(request):
    articles = Article.objects.all().order_by("date")
    paginator = Paginator(articles, 3)
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
    paginator = Paginator(articles, 3)
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

    article.views=article.views+1
    article.save()


    return render(request,'articles/article_detail.html', {'article': article, 'tags': tags, 'related_articles': related_articles})

def category_list(request):
    categories = Category.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    
    return render (request, 'articles/categories_list.html', {'categories': categories}) 

def category_detail(request, slug):
    selected_category = Category.objects.get(slug = slug)
    category_title = selected_category.title
    articles = Article.objects.filter(category__slug__exact = slug)
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles/category_detail.html', {'category': selected_category.title, 'articles': articles, 'page': page}) 

def homepage(request):
    articles = Article.objects.all().order_by("-date")
    tags = Tag.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        articles = paginator.page(paginator.num_pages)
    top_articles = Article.objects.all().order_by("-views")
    

    return render(request, "articles/homepage.html", {'page': page,'articles': articles, 'tags': tags, 'categories': categories, 'top_articles': top_articles[0:3]})
