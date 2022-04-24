from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    # authors = models.ManyToManyField(Author)
    authors = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, models.PROTECT)
