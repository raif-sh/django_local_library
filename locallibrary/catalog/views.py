from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # generate counts of genres and books containing word `galaxy`
    num_genres = Genre.objects.count()
    num_books_galaxy = Book.objects.filter(title__icontains='galaxy').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_galaxy': num_books_galaxy,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):     
    model = Author     
    paginate_by = 10  
    
class AuthorDetailView(generic.DetailView):     
    model = Author 