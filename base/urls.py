"""urlconf for the base application"""

from django.conf.urls import include, patterns, url
from .views import MovieList,MovieDetail

urlpatterns = patterns('base.views',
    
)
