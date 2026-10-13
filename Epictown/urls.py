from django.urls import path
from . import views
from .views import (
    ComicbookListView,
    ComicbookCreateView,
    ComicbookDetailView,
    ComicbookEditView,
    ComicbookDeleteView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('dashboard', ComicbookListView.as_view(), name='dashboard'),
    path('products/<int:pk>', ComicbookDetailView.as_view(), name='product-view'),
    path('product/new', ComicbookCreateView.as_view(), name='create'),
    path('product/edit/<int:pk>', ComicbookEditView.as_view(), name='edit'),
    path('product/delete/<int:pk>', ComicbookDeleteView.as_view(), name='delete'),
    path('products/search', views.search, name='search'),
    path('login', auth_views.LoginView.as_view(template_name='navbar/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register', views.register, name='register'),
]