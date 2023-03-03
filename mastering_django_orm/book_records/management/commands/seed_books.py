from django.core.management import BaseCommand

from mastering_django_orm.book_records.factories import BookFactory


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--batch_size',
            type=int,
            required=True,
            help='Amount of Books we wish to generate.'
        )

    def handle(self, *args, **options):
        batch_size = options.get('batch_size', 2)
        self._generate_books(batch_size)

    def _generate_books(self, batch_size):
        BookFactory.create_batch(size=batch_size)
