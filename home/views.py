from operator import mod
from unicodedata import category
from django.shortcuts import render
from . import models
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    category_list=models.Category.objects.all()
    paginator=Paginator(models.Anime.objects.filter(status='MW'),9)
    page_number = request.GET.get('page')
    anime_list = paginator.get_page(page_number)
    paginator1=Paginator(models.Anime.objects.filter(status='RA'),9)
    page_number1 = request.GET.get('page1')
    anime_list1 = paginator1.get_page(page_number1)
    paginator2=Paginator(models.Anime.objects.filter(status='TR'),9)
    page_number2 = request.GET.get('page2')
    anime_list2 = paginator2.get_page(page_number2)
    context={'anime_list':anime_list,'anime_list1':anime_list1,'anime_list2':anime_list2,'category_list':category_list}
    return render(request,'index.html',context)
def watching(request,epslug):
    category_list=models.Category.objects.all()
    details=False
    try:
        episode=models.Episodes.objects.get(epslug=epslug)
    except:
        episode=models.Episodes.objects.get(epslug=epslug+'1')
        details=True
    episode_list=models.Episodes.objects.filter(epanmname=episode.epanmname)
    context={'episode':episode,'episode_list':episode_list,'details':details,'category_list':category_list}
    return render(request,'watching.html',context)
def search(request):
    category_list=models.Category.objects.all()
    search_words=request.POST.get('search_words')
    anime_list=models.Anime.objects.filter(title__contains=str(search_words))
    context={'anime_list':anime_list,'category_list':category_list,'search_words':search_words}
    return render(request,'resulte_page.html',context)

def categories(request,categories):
    category_list=models.Category.objects.all()
    category=models.Category.objects.get(catname=categories)
    anime_list=models.Anime.objects.filter(category=category)
    context={'anime_list':anime_list,'category_list':category_list,'category':category}
    return render(request,'categories.html',context)