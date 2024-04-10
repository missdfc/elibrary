from django.db import models

# Create your models here.

# creating model for books database first, going to create each field that makes a book
class Books(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    preview = models.TextField()
    content = models.TextField()
    genere = models.CharField(max_length=500)
    publisher = models.CharField(max_length=500)
    date_published = models.DateField(null=True, blank=True)
    file_type = models.CharField(max_length=500)
    isbn = models.CharField(max_length=500)
    review = models.TextField()
    no_available_books = models.PositiveIntegerField()
    borrowed_books = models.IntegerField()

    def __str__(self):
        return self.title

