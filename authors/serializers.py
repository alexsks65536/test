# from rest_framework import serializers
# from .models import Author, Book, Biography, Article
#
#
# class AuthorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#
# class BiographySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Biography
#         fields = '__all__'
#
#
# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class BookSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'
from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # Authors = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

