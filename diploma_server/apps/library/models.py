from django.db import models
from apps.language.models import Language
from apps.user.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    logo = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Sentence(models.Model):
    text = models.CharField(max_length=255)
    audio = models.CharField(max_length=255)
    translate = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} sentence added"

class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"