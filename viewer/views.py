from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from .models import Author, Genre, Book


# Create your views here.


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class AuthorView(ListView):
    template_name = 'authors.html'
    model = Author


class AuthorDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'author_detail.html'
    model = Author
    permission_required = 'viewer.view_author'


class AuthorCreateView(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('authors')
    permission_required = 'viewer.add_author'


class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('authors')
    permission_required = 'viewer.change_author'


class AuthorDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Author
    template_name = "author_delete.html"
    success_url = reverse_lazy('authors')
    permission_required = 'viewer.delete_author'


class GenreView(ListView):
    template_name = 'genres.html'
    model = Genre


class GenreDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'genre_detail.html'
    model = Genre
    permission_required = 'viewer.view_genre'


class GenreCreateView(PermissionRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.add_genre'


class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.change_genre'


class GenreDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Genre
    template_name = "genre_delete.html"
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.delete_genre'


class BookView(ListView):
    template_name = 'books.html'
    model = Book
    paginate_by = 2

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class BookDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'book_detail.html'
    model = Book
    permission_required = 'viewer.view_book'


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy('books')
    permission_required = 'viewer.add_book'


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')
    permission_required = 'viewer.change_book'


class BookDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy('books')
    permission_required = 'viewer.delete_book'
