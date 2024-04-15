from django.db import models

# creating model for database first, going to create each field that makes the model

# genere model
class Genere(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# file type(e.g pdf, epub) model
class FileType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# models for the elibrary users
class ElibraryUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

'''RATINGS = (('1', '1'), ('2','2'))
class Review(models.Model):
    user = models.ForeignKey()
    ratings = models.CharField(max_length=100, choices=RATINGS)'''

# books model
class Books(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    preview = models.TextField()
    content = models.TextField()
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=500)
    date_published = models.DateField()
    file_type = models.ForeignKey(FileType, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=500)
    review = models.TextField(null=True, blank=True)
    no_available_books = models.PositiveIntegerField()
    borrowed_books = models.IntegerField()

    def __str__(self):
        return self.title

