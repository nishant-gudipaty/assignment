from django.shortcuts import render
from django.http import HttpResponse
from .models import BookModel, UserModel

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import *
# Create your views here.


class BookView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user):
        books = BookModel.objects.filter(user=user)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookEditSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user, pk=None):
        queryset = BookModel.objects.filter(user=user)
        book = get_object_or_404(queryset,pk =pk)
        serializer = BookListSerializer(book)
        return Response(serializer.data)

    def put(self,request, user, pk=None):
        book = BookModel.objects.filter(user=user).get(pk=pk)
        serializer = BookEditSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user, pk=None):
        book = BookModel.objects.filter(user=user).get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user):
        userdb = UserModel.objects.filter(pk=user)
        if userdb.user_type == "SU":
            users = UserModel.objects.all()
            serializer = UserListSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)

    def post(self, request, user):
        userdb = UserModel.objects.filter(pk=user)
        if userdb.user_type == "SU":
            serializer = UserEditSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user, pk=None):
        userdb = UserModel.objects.filter(pk=user)
        if userdb.user_type == "SU":
            queryset = BookModel.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = UserListSerializer(user)
            return Response(serializer.data)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)

    def put(self,request, user, pk=None):
        userdb = UserModel.objects.filter(pk=user)
        if userdb.user_type == "SU":
            user = UserModel.objects.all().get(pk=pk)
            serializer = UserEditSerializer(user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, user,  pk=None):
        userdb = UserModel.objects.filter(pk=user)
        if userdb.user_type == "SU":
            user = UserModel.objects.all().get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)