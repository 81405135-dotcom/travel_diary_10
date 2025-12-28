from django.urls import path
from .views import (
    home,
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    SignUpView, MyPostListView,contact
)

urlpatterns = [
    path('', home, name='home'),

    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('my/', MyPostListView.as_view(), name='my_posts'),

    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('contact/', contact, name='contact'),

]

