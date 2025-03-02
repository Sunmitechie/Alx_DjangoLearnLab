from django.urls import path
<<<<<<< HEAD
from relationship_app.views import list_books, LibraryDetailView, register_view, login_view, logout_view  # Replace 'your_actual_app_name' with the actual app name
=======
from relationship_app.views import list_books, LibraryDetailView  
>>>>>>> 0b95bdeb56b88e1182e4eb55cfc16a96532f1f41
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
