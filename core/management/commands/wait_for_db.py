"""
Django command to wait for database to be available
"""
from django.core.management.base import BaseCommand


class COmmand(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        pass