from django .urls import path
from . import views

urlpatterns = [
    path('', views.Blog_post, name='Blog_post'),
    path("<int:pk>/", views.blog_index, name="blog_index"),
]