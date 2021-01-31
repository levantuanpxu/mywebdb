from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
# Create your views here.
from myapp.models import Post, Categories
from django.core.paginator import Paginator


def home(request):
    cate = Categories.objects.all()
    posts = Post.objects.all()
    top6 = Paginator(posts, 4)
    top4 = Paginator(posts, 3)
    page_num = request.GET.get('page')
    page = top4.get_page(page_num)
    top6 = Paginator(posts, 4)
    pages = top6.get_page(page_num)
    top1 = Paginator(posts, 1)
    page1 = top1.get_page(page_num)
    context = {
        'posts': posts,
        'cate': cate,
        'top4': top4.count,
        'page': page,
        'pages': pages,
        'page1': page1,

    }

    return render(request, 'pages/home_page01.html', context)

def list(request):

    posts = Post.objects.all()
    context = {

        'posts': posts
    }

    return render(request, 'pages/list.html', context )

class HomeDetailView(DetailView):

    model = Post

    template_name = 'pages/detail.html'

class ListDetailView(DetailView):

    model = Post
    template_name = 'pages/detaillist.html'