from django.urls import path
from relationship_app.views import list_books, LibraryDetailView, register_view
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app.views import list_books, LibraryDetailView  
from .views import list_books
from django import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
