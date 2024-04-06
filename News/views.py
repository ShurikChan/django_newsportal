from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_post'] = "Пока нет новостей!"
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'readpost.html'
    context_object_name = 'postd'