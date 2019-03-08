# blog/urls.py
from django.urls import path
from . import views
 
urlpatterns = [
path('', views.BlogListView.as_view(), name='home'),
path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
path('post/new_out/', views.Blog_out_CreateView.as_view(), name='post_new_out'),
path('post/new_in/', views.Blog_in_CreateView.as_view(), name='post_new_in'),
path('post/<int:pk>/edit/',
views.BlogUpdateView.as_view(), name='post_edit'),
]

