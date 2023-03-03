from django.core.management import BaseCommand

from mastering_django_orm.book_records.models import Book, Author, Publisher


class Command(BaseCommand):

    def handle(self, *args, **options):
        books = Book.objects.all()
        authors = Author.objects.all()
        publishers = Publisher.objects.all()

        books.delete()
        authors.delete()
        publishers.delete()
