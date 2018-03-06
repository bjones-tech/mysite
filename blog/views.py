from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.utils import timezone

from .models import Post


def index(request):
    published_posts = get_list_or_404(Post.objects.exclude(publish_date=None).order_by('-publish_date'),
                                      publish_date__lte=timezone.now())
    return render(request, 'blog/index.html', {'posts': published_posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
