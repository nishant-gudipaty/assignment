from rest_framework import serializers
from .models import BookModel, UserModel


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        exclude = ['user']


class BookEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ['password']

