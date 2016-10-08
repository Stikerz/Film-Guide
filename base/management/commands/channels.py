from django.core.management.base import BaseCommand, CommandError
from base.models import Channels

import requests

class Command(BaseCommand):
	def handle(self, *args, **options):
		r = requests.get('https://atlas.metabroadcast.com/3.0/channel_groups/cbg4.json?annotations=channels')
		channel_groups = r.json()['channel_groups'][0]
		for channel in channel_groups['channels']:
			Channels.objects.get_or_create(
				title=channel['channel']['title'],
				channel_id=channel['channel']['id']
			)