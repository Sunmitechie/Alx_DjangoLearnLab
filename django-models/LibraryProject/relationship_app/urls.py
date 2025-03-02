from django.urls import path
from relationship_app.views import list_books, LibraryDetailView, register_view, login_view, logout_view  
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
