from unicodedata import category
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import AnimeSerializer, CatSerializer, EpSerializer
from django.db.models import Q
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
        episode=models.Episodes.objects.get(epslug=epslug+'-ep-'+'1')
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
class AnimeListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = models.Anime.objects.all()
        serializer = AnimeSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Anime_imgListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        id=request.query_params['anime_id']
        todos = models.Anime.objects.filter(id=id)
        serializer = AnimeSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnimeoDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        id=request.query_params['id']
        todos = models.Episodes.objects.filter(epanmname=id)
        serializer = EpSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CatDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        id=request.query_params['cat_id']
        todos = models.Category.objects.filter(id=id)
        serializer = CatSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EpsApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = models.Episodes.objects.all().order_by("-id")
        serializer = EpSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Anime_SearchListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        keyword=request.query_params['keyword']
        try:
            todos = models.Anime.objects.filter(category=int(keyword))
            print("int")
        except:
            todos = models.Anime.objects.filter(Q(title__icontains=str(keyword))|Q(studio=str(keyword)))
        serializer = AnimeSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Catgories_ListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = models.Category.objects.all()
        serializer = CatSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)