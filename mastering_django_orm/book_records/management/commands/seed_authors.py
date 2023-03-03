from django.core.management import BaseCommand

from mastering_django_orm.book_records.factories import AuthorFactory


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--batch_size',
            type=int,
            help='Amount of authors we wish to generate.'
        )

    def handle(self, *args, **options):
        batch_size = options.get('batch_size', 2)
        self._generate_authors(batch_size)

    def _generate_authors(self, batch_size):
        AuthorFactory.create_batch(size=batch_size)
