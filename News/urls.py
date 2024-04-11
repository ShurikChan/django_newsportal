from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, NewsUpdate,ProductDelete


urlpatterns = [
   path('', PostList.as_view(), name='post_main'), 
   path('<int:pk>', PostDetail.as_view()), 
   path('search', PostSearch.as_view()),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', ProductDelete.as_view(), name='news_delete'),
]