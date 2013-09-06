import logging
import os
import urllib2
import datetime

from django.core.management.base import BaseCommand
from django.conf import settings

from jellyroll.models import Photo
from jellyroll.providers.flickr import FlickrClient
from jellyroll.providers import utils

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        level = {
            '0': logging.WARN,
            '1': logging.INFO,
            '2': logging.DEBUG
        }[options.get('verbosity', '0')]
        logging.basicConfig(level=level, format="%(name)s: %(levelname)s: %(message)s")

        local_photos = Photo.objects.all()

        flickr = FlickrClient(settings.FLICKR_API_KEY)
        for photo in local_photos:
            if not photo.farm_id:
                #import pdb; pdb.set_trace()
                info = flickr.photos.getInfo(photo_id=photo.photo_id, secret=photo.secret)["photo"]  
                photo.farm_id = info['farm']
                photo.save()
