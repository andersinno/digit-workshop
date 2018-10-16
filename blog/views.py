from django.http import Http404
from django.shortcuts import render
from django.utils import timezone

from blog.models import BlogPost


def index(request):
    blog_posts = BlogPost.objects.filter(date__lte=timezone.now())

    return render(request, 'blog/index.html', {
        'blog_posts': blog_posts,
    })


def post_detail(request, post_id):
    try:
        blog_post = BlogPost.objects.filter(date__lte=timezone.now()).get(pk=post_id)
    except BlogPost.DoesNotExist:
        raise Http404('Post does not exist')

    return render(request, 'blog/detail.html', {
        'blog_post': blog_post,
    })
