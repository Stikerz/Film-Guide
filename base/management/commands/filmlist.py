from django.core.management.base import BaseCommand, CommandError
from base.models import FilmList

import config
import requests

class Command(BaseCommand):
	def handle(self, *args, **options):
		api_url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s" % (config.rotten_api_key)
		response = requests.get(api_url).json()
		for data in response['movies']:
			obj, created = FilmList.objects.get_or_create(
				title=data['title'],
			)
			obj.thumbnail = data['posters']['thumbnail']
			obj.profile = data['posters']['profile']
			obj.detailed = data['posters']['detailed']
			obj.original = data['posters']['original']
			obj.save()

		