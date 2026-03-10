from django.urls import path
from . import views
from .views import (
    ListView,
    CreateView,
    DetailView,
    EditView,
    DeleteView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('dashboard', ListView.as_view(), name='dashboard'),
    path('products/<int:pk>', DetailView.as_view(), name='product-view'),
    path('product/new', CreateView.as_view(), name='create'),
    path('product/edit/<int:pk>', EditView.as_view(), name='edit'),
    path('product/delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('products/search', views.search, name='search'),
    path('login', auth_views.LoginView.as_view(template_name='navbar/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register', views.register, name='register'),
]