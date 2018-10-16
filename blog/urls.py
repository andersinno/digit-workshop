from django.urls import path

from blog.views import index, post_detail

urlpatterns = [
    path('', index, name='blog-index'),
    path('post/<int:post_id>/', post_detail, name='blog-detail'),
]
