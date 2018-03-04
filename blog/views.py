from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Post


def index(request):
    published_posts = get_list_or_404(Post.objects.order_by('-created'), published=True)
    return render(request, 'blog/index.html', {'posts': published_posts})
