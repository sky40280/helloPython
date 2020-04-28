from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=127)
    page = models.IntegerField()
    isbn = models.CharField(max_length=31)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "books"
