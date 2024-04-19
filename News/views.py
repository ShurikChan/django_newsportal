from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .filters import PostFilter
from .forms import NewsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
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
    
class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_post', )
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsUpdate(LoginRequiredMixin ,PermissionRequiredMixin, UpdateView):
    permission_required = ('News.change_post', )
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('News.delete_post', )
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_main')