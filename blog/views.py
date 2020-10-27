from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *

def home(request):
    posts =  Post.objects.all().order_by('-date_posted')[:3]
    return render(request, 'blog/home.html', {'title': "Home", 'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': "About",})

def post(request, postId):
    post = Post.objects.get(id=postId)
    return render(request, 'blog/post.html', {'title': "Post", 'post': post})

def contact(request):
    return render(request, 'blog/contact.html', {'title': "Contact",})

class CategoriesListView(ListView):
    model = Category
    template_name = 'blog/categories.html'
    context_object_name = 'categories'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categories'
        return context

class ArticlesListView(ListView):
    model = Post
    template_name = 'blog/articles.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self,**kwargs):
        category = get_object_or_404(Category, id=self.kwargs['categoryId'])
        return Post.objects.filter(category=category).order_by('-date_posted')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Articles'
        context['category'] = Category.objects.get(id=self.kwargs['categoryId'])
        return context