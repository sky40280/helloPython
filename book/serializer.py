from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'page',
            'isbn',
            'created_at',
            'updated_at',
        ]
