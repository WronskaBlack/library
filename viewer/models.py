from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    publication_date = models.DateField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
