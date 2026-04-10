from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def show(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/show.html', {'book': book})


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            if Book.objects.filter(title=form.cleaned_data['title']).exists():
                form.add_error('title', 'This title already exists.')
            else:
                book = Book.objects.create(
                    title=form.cleaned_data['title'],
                    breif=form.cleaned_data['breif'],
                    image=form.cleaned_data.get('image'),
                    no_of_page=form.cleaned_data['no_of_page'],
                    price=form.cleaned_data['price'],
                )

                book.authors.set(form.cleaned_data['authors'])

                return redirect('books:index')
    else:
        form = BookForm()

    return render(request, 'books/create.html', {'form': form})

def update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            old_book = Book.objects.filter(title=form.cleaned_data['title']).exclude(id=book.id)
            if old_book.exists():
                form.add_error('title', 'This title already exists.')
            else:
                book.title = form.cleaned_data['title']
                book.breif = form.cleaned_data['breif']
                book.no_of_page = form.cleaned_data['no_of_page']
                book.price = form.cleaned_data['price']

                if request.FILES.get('image'):
                    book.image = form.cleaned_data['image']

                book.save()
                book.authors.set(form.cleaned_data['authors'])

                return redirect('books:show', id=book.id)
    else:
        form = BookForm(initial={
            'title': book.title,
            'breif': book.breif,
            'no_of_page': book.no_of_page,
            'price': book.price,
            'authors': book.authors.all(),
        })

    return render(request, 'books/update.html', {'form': form, 'book': book})

def delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('books:index')

    return render(request, 'books/delete.html', {'book': book})