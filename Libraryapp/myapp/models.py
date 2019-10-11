from django.db import models


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    isbn = models.IntegerField()
    author_name = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
