from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL


class Command(BaseCommand):
    help = "Refresh all KirrURL shortcodes"

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)


    def handle(self, *args, **options):
        print(options)
        return KirrURL.objects.refresh_shortcodes(items=options['items'])
