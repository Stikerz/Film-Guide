""" Default urlconf for movie_app """

from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()

from base.views import MovieList,MovieDetail,Profile

def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movie_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', MovieList.as_view(), name='home'),
    url(r'^profile/', Profile.as_view(), name='profile'),
    url(r'^movies/', MovieList.as_view(), name='movie_list'),
    url(r'^movieDetail/(?P<id>.+?)/$', MovieDetail.as_view(), name='movie_detail'),
)

