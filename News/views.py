from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, Category, Author
from .filters import PostFilter
from .forms import NewsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.utils.translation import gettext as gettext


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
        context['next_post'] = gettext("Пока нет новостей!")
        context['filterset'] = self.filterset
        context['allposts'] = Post.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'readpost.html'
    context_object_name = 'postd'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj


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
        context['next_post'] = gettext("Пока нет новостей!")
        context['filterset'] = self.filterset
        return context


class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_post', )
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.get(user=self.request.user)
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(user=self.request.user)
        post.save()
        return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('News.change_post', )
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('News.delete_post', )
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_main')


@login_required
def subscribe(request, pk):
    category = Category.objects.get(pk=pk)
    user = request.user
    category.subscribers.add(user)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def unsubscribe(request, pk):
    category = Category.objects.get(pk=pk)
    user = request.user
    category.subscribers.remove(user)
    return redirect(request.META.get('HTTP_REFERER'))
