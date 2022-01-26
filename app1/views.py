from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import *
from django.contrib import messages
# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'app1/home.html'
    oredering = ['-date']

    extra_context = {'categories':Category.objects.all()}

class Detail(DetailView):
    model = Post
    template_name = 'app1/detail.html'
class Add(CreateView):
    model = Post
    form_class = PostForm
    template_name= 'app1/create.html'
class Edit(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'app1/edit.html'
class Delete(DeleteView):
    model = Post
    template_name = 'app1/delete.html'
    success_url=reverse_lazy('home_view')


class AddCat(CreateView):
    model = Category
    template_name= 'app1/category.html'
    fields = '__all__'
def Catdetail(request,var):
    posts = Post.objects.filter(category=var)
    return render(request,'app1/catdetail.html',{'var':var,'posts':posts})
def Catlist(request):
    categories  = Category.objects.all()
    return render(request,'app1/catlist.html',{'var':categories})
