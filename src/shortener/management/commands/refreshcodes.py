from django.core.management.base import BaseCommand, CommandError
#This file has custom Management commands
from shortener.models import ShorURL

class Command(BaseCommand):
    help = 'Refreshes all ShorURL shortcodes'

    

    def handle(self, *args, **options):
        return ShorURL.objects.refresh_shortcode()
       