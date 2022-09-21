from django.shortcuts import render, get_object_or_404
from rest_framework import status, request
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from first_app import serializer
from first_app.models import Book, Publisher
from first_app.serializer import BookSerializer, BookCreateSerializer, PublisherSerializer


# Create your views here.

# def index(request):
#     name = "Tobi"
#     return render(request, 'index.html', context={"name": name})
#
# def redirect(request):
#     return HttpResponseRedirect(reverse('first_app:hello'))
#
#
# def hello(request, name: str, num: int):
#     return HttpResponse(f"<h1>Hello {num}. {name.title()}, Welcome to Django</h1>")
#
#
# def book_list(request):
#     books = Book.objects.all()
#     # books = Book.objects.filter(genre= 'ROMANCE')
#     books = Book.objects.filter(price__gt=50.00)
#     return render(request, 'first_app/book-list.html', {'books': list(books)})
#
#
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return render(request, 'first_app/book-detail.html', {'book': book})

# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(request, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     def post(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     # def get_serializer_class(self):
#     #     if self.request.method == 'GET':
#     #         return BookSerializer
#     #     else:
#     #         return BookCreateSerializer
#
#
# class BookDetail(APIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class PublisherList(APIView):
    def get(self, request):
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, context={'request': self.request})
        return Response(serializer.data)

    def post(self):
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PublisherDetails(APIView):
    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        serializer = PublisherSerializer(publisher, context={'request': self.request})
        return Response(serializer.data)

    def patch(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        serializer = BookSerializer(publisher, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        publisher.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

