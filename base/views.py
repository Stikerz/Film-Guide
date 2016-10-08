""" Views for the base application """

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import FilmList

import config
import requests

class MovieList(TemplateView):
	template_name = 'movie/movie_listing.html'
	def get(self, request, *args, **kwargs):
		# Get the url params
		query = request.GET.get('query')
		if query:
			# Enter here if searched
			movies = FilmList.objects.filter(title__icontains=query)
		else:
			# By default list all
			movies = FilmList.objects.all()
		return render(request,self.template_name,{'movies': movies})

class MovieDetail(TemplateView):
	template_name = 'movie/movie_detail.html'
	def get(self, request, id, *args, **kwargs):
		# Get the url params and send to rottn api
		query = request.GET.get('q')
		movie = FilmList.objects.filter(id=id)[0]
		movie_url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=%s&q=%s&page_limit=1" % (config.rotten_api_key, query)
		response = requests.get(movie_url).json()
		return render(request,self.template_name,{'movie': response['movies'][0]})

class Profile(TemplateView):
	template_name = 'profile/account.html'
	def get(self, request, *args, **kwargs):
		user = request.user
		return render(request,self.template_name,{'user': user})
