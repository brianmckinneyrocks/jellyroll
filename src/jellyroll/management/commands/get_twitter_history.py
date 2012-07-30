import logging
import optparse
import jellyroll.providers
from django.core.management.base import BaseCommand
from jellyroll.providers import twitter

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        level = {
            '0': logging.WARN,
            '1': logging.INFO,
            '2': logging.DEBUG
        }[options.get('verbosity', '0')]
        logging.basicConfig(level=level, format="%(name)s: %(levelname)s: %(message)s")
 
        twitter.get_history()
