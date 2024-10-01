from django.urls import path
from . import views

# create your urls here

app_name = 'blog'

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('detail/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:post_pk>/', views.CommentCreateView.as_view(), name='create_comment'),
    path('cat/<slug:slug>/', views.FilterPostsByCategory.as_view(), name='filter_posts_by_category'),
]
