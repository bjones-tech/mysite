from django.shortcuts import render, get_list_or_404

from .models import ContentRow


def index(request):
    return render(request, 'home/index.html')


def about(request):
    content_rows = get_list_or_404(ContentRow, page='ABOUT')
    return render(request, 'home/about.html', {'content_rows': content_rows})


def contact(request):
    content_rows = get_list_or_404(ContentRow, page='CONTACT')
    return render(request, 'home/contact.html', {'content_rows': content_rows})
