from django.urls import path
from . import views
from .views import CategoriesListView, ArticlesListView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('categories/', CategoriesListView.as_view(), name='blog-categories'),
    path('categories/<int:categoryId>', ArticlesListView.as_view(), name='blog-category'),
    path('post/<int:postId>', views.post, name='blog-post'),
]