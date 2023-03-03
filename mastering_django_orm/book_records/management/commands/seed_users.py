from django.core.management.base import BaseCommand

from mastering_django_orm.book_records.models import User


class Command(BaseCommand):
    help = 'Seed the User table.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--amount',
            type=int,
            help='The amount of users we are adding to our database.'
        )

    def handle(self, *args, **options):
        amount = options.get('amount', 100)
        self._generate_users(amount)

    def _generate_users(self, amount):
        pass


