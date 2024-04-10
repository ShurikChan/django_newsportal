import django_filters
from django_filters import FilterSet
from .models import Post
from django_filters.widgets import RangeWidget

class PostFilter(FilterSet):
   time_in = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))
   class Meta:
       model = Post
       fields = {
           'heading': ['icontains'],
           'author' : ['exact'],
           
       }
