from django.http import Http404
from django.shortcuts import render

from blog.models import BlogPost


def index(request):
    blog_posts = BlogPost.objects.public()

    return render(request, 'blog/index.html', {
        'blog_posts': blog_posts,
    })


def post_detail(request, post_id):
    try:
        blog_post = BlogPost.objects.public().get(pk=post_id)
    except BlogPost.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'blog/detail.html', {
        'blog_post': blog_post,
    })
