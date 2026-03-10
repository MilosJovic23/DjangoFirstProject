from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Epictown.forms import RegistrationForm, LoginForm
from Epictown.models import Comicbook


def index(request):
    comics = Comicbook.objects.all()
    return render(request, 'index.html', {'comics': comics})

def about(request):
    return render(request, 'navbar/about.html')

def blog(request):
    return render(request, 'navbar/blog.html')

class ListView( LoginRequiredMixin, ListView ):
    model = Comicbook
    template_name = 'navbar/dashboard.html'
    context_object_name = 'comicbook'

class CreateView(  LoginRequiredMixin,SuccessMessageMixin, CreateView ):
    model = Comicbook
    template_name = 'create.html'
    fields = ['title','description','format','ImgUrl','author','rating']
    success_message = "You have successfully created the comicbook"

    def get_success_url(self):
        return reverse_lazy('product-view', kwargs={'pk': self.object.pk })

class DetailView( DetailView ):
    model = Comicbook
    template_name = 'detail.html'

class EditView( LoginRequiredMixin, SuccessMessageMixin, UpdateView ):
    model = Comicbook
    template_name = 'edit.html'
    fields = ['title','description','format','ImgUrl','author','rating']
    success_url = reverse_lazy('dashboard')
    success_message = "You have successfully edited the comicbook"

class DeleteView( LoginRequiredMixin, SuccessMessageMixin, DeleteView ):
    model = Comicbook
    template_name = 'delete.html'
    success_url = reverse_lazy('dashboard')
    success_message = "You have successfully deleted the comicbook"

def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search','')
        if search_query:
            result = Comicbook.objects.filter(title__icontains=search_query)
            return render(request, 'navbar/search.html', {'comicbooks': result })
        else:
            return render(request, 'navbar/search.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Congrats! Your account has been created!')
            return redirect('login')
    else :
        form = RegistrationForm()
    return render(request, 'navbar/register.html',{'form':form})
