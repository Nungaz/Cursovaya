from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogIndex.as_view(), name='index'),
    path('blogs/', Blogs.as_view(), name='blogs'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('addimg/', AddImg.as_view(), name='addimg'),
]
