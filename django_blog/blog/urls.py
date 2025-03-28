from django import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view, add_comment, search_posts
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentDeleteView, CommentUpdateView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('comment/<int:pk>/update/', "post/<int:pk>/comments/new/", 'comment/<int:pk>/delete/'),
    path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', PostListView.as_view(), name='posts-by-tag'),
    path('tags/<str:tag_name>/posts/', PostListView.as_view(), name='posts-by-tag')
    path("tags/<slug:tag_slug>/", "PostByTagListView.as_view()", name="posts-by-tag")
]
