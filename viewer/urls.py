from django.urls import path
from .views import (AuthorView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
                    BookView, BookDetailView, BookDeleteView, BookCreateView, BookUpdateView,
                    GenreView, GenreDetailView, GenreDeleteView, GenreUpdateView, GenreCreateView)

urlpatterns = [
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    path('genres/', GenreView.as_view(), name='genres'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('genres/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genres/update/<int:pk>', GenreUpdateView.as_view(), name='genre_update'),
    path('genres/delete/<int:pk>', GenreDeleteView.as_view(), name='genre_delete'),
    path('books/', BookView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

]

