from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.urls import reverse_lazy
from .forms import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import LoginForm


class BlogIndex(DataMixin, CreateView):
    form_class = RegUserForm
    template_name = 'blog/index.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(c_def.items()) + list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blogs')

    def get_queryset(self):
        return Blog.objects.filter(published=True).select_related('cat')


class Blogs(DataMixin, ListView):
    model = Blog
    template_name = "blog/blog.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Блог")
        return dict(list(c_def.items()) + list(context.items()))

    def get_queryset(self):
        return Blog.objects.filter(published=True).select_related('cat')


class ShowPost(DataMixin, DetailView):
    model = Blog
    template_name = "blog/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"])
        return dict(list(c_def.items()) + list(context.items()))


class BlogCategory(DataMixin, ListView):
    model = Blog
    template_name = "blog/blog.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title="Категория - " + str(c.name), cat_selected=c.pk)
        return dict(list(c_def.items()) + list(context.items()))


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForms
    template_name = 'blog/addpost.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(c_def.items()) + list(context.items()))


class AddImg(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddImgForms
    template_name = 'blog/addimg.html'
    success_url = reverse_lazy('blogs')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление картинки")
        return dict(list(c_def.items()) + list(context.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(c_def.items()) + list(context.items()))


class LogoutUser(DataMixin, ListView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('blogs')
