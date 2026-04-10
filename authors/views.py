from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/index.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/show.html'
    context_object_name = 'author'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/create.html'
    success_url = reverse_lazy('authors:index')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/update.html'
    success_url = reverse_lazy('authors:index')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete.html'
    success_url = reverse_lazy('authors:index')