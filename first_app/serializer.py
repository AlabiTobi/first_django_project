from rest_framework import serializers
from first_app.models import Book, Publisher


class BookSerializer(serializers.ModelSerializer):  # noqa
    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn', 'price']


class BookCreateSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(max_length=255, source='title')

    class Meta:
        model = Book
        fields = ['book_title', 'description', 'isbn', 'price', 'date_published', 'publisher']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']

