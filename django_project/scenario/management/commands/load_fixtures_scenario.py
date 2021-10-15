import os
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """
    Update all fixtures
    """

    def handle(self, *args, **options):
        call_command('load_fixtures_core')
        call_command('loaddata', 'scenario/fixtures/fixtures.json')
