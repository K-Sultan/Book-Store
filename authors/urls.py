from django.urls import path
from .views import *

app_name = 'authors'

urlpatterns = [
    path('', AuthorListView.as_view(), name='index'),
    path('create/', AuthorCreateView.as_view(), name='create'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='show'),
    path('<int:pk>/update/', AuthorUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='delete'),
]