from datetime import datetime, timedelta
import factory
from factory.django import DjangoModelFactory

from mastering_django_orm.book_records.models import Author, Publisher, Book


class PublisherFactory(DjangoModelFactory):
    class Meta:
        model = Publisher

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    join_date = factory.Faker('date_between', start_date=datetime.now() - timedelta(days=5475), end_date=datetime.now())
    popularity_score = factory.Faker('pyfloat', left_digits=2, min_value=0.00, max_value=5.00)


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    address = factory.Faker('street_address')
    zipcode = factory.Faker('postcode')
    telephone = factory.Faker('phone_number')
    join_date = factory.Faker('date_between', start_date=datetime.now() - timedelta(days=5475), end_date=datetime.now())
    popularity_score = factory.Faker('pyfloat', left_digits=2, min_value=0.00, max_value=5.00)
    recommended_by = factory.SubFactory(PublisherFactory)


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('text', max_nb_chars=20)
    genre = factory.Faker('color')
    price = factory.Faker('pyfloat', left_digits=2, min_value=5.00, max_value=25.00)
    published_date = factory.Faker('date_between', start_date=datetime.now() - timedelta(days=5475))
    author = factory.Faker('name')
    publisher = factory.SubFactory(PublisherFactory)
