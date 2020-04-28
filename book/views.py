from rest_framework import viewsets

from book.models import Book
from book.serializer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
