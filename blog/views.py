from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from . models import Post
class BlogListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'  

class Blog_out_CreateView(CreateView):
    model = Post
    template_name = 'post_new_out.html'
    fields = ['title', 'body']
    
class Blog_in_CreateView(CreateView):
    model = Post
    template_name = 'post_new_out.html'
    fields = ['title', 'body']    
    
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'    
    
class BlogDetailView_Inposts(DetailView):
    model = Post
    template_name = 'post_detail.html' 
  #  queryset = Post.objects.filter(in_number__name='ACME Publishing')