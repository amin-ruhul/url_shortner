from django.core.management.base import BaseCommand, CommandError 

from shortner.models import UrlShortner 

class Command(BaseCommand):
    help = 'Refresh all url short code'


    def handle(self,*args,**options):
        return UrlShortner.objects.refresh_shortner()
