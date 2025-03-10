from rest_framework import serializers
from .models import Book, Sentence, FavoriteBook


class BookSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'language', 'logo')

class SentenceSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Sentence
        fields = ('id', 'text', 'audio', 'translate', 'book')

class FavoriteBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = FavoriteBook
        fields = ('id', 'user', 'book')
        read_only_fields = ('user', )