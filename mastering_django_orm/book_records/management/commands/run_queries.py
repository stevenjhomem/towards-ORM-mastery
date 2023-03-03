from django.core.management import BaseCommand
import sqlparse
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from django.db.models import QuerySet

from mastering_django_orm.book_records.models import Book, Publisher, Author


class Command(BaseCommand):

    def handle(self, *args, **options):
        def print_sql(queryset: QuerySet):
            formatted = sqlparse.format(str(queryset.query), reindent=True)
            print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

        qs_1 = Book.objects.all()

        return print_sql(qs_1)
