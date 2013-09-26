import logging
import os
import urllib2
import datetime

from django.core.management.base import BaseCommand
from django.conf import settings

from jellyroll.models import Photo

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        level = {
            '0': logging.WARN,
            '1': logging.INFO,
            '2': logging.DEBUG
        }[options.get('verbosity', '0')]
        logging.basicConfig(level=level, format="%(name)s: %(levelname)s: %(message)s")
       
        path = 'photos/flickr/%Y/%m/%d'
        today = datetime.datetime.today()
        desired_path = os.path.join(settings.MEDIA_ROOT, today.strftime(path))

        if not os.path.exists(desired_path):
            os.makedirs(desired_path)

        photos = Photo.objects.filter(local_image="")

        for photo in photos:
            image_temp = urllib2.urlopen(photo.original_url)
            image = image_temp.read()
            image_name = photo.original_url.split('/')[-1]
            dest = open(os.path.join(desired_path, image_name), 'wb+')
            dest.write(image) 
            photo.local_image = os.path.join(today.strftime(path), image_name) 
            photo.save()
            dest.close()
