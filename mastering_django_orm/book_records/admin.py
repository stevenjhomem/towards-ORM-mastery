from django.contrib import admin

from mastering_django_orm.book_records.models import Author, Book, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = [
        'id',
        'first_name',
        'last_name',
        'address',
        'zipcode',
        'telephone',
        'recommended_by',
        'join_date',
        'popularity_score',
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = [
        'id',
        'title',
        'genre',
        'price',
        'published_date',
        'author',
        'publisher',
    ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    model = Publisher
    list_display = [
        'id',
        'first_name',
        'last_name',
        'join_date',
        'popularity_score',
    ]
