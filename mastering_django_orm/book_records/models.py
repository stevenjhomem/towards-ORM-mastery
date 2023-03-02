from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    telephone = models.CharField(max_length=100, null=True)
    recommended_by = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True)
    join_date = models.DateField()
    popularity_score = models.IntegerField()
    followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Books(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', related_query_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books')

    def __str__(self):
        return self.title


class Publisher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    recommended_by = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
    join_date = models.DateField()
    popularity_score = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username
