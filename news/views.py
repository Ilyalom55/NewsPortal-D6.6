from django.views.generic import ListView, DetailView

from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-post_time_in'
    template_name = 'post_list.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'
