from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_post'] = "Пока нет новостей!"
        context['filterset'] = self.filterset
        
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'readpost.html'
    context_object_name = 'postd'