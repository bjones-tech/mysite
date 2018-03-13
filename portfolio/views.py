from django.shortcuts import render, get_list_or_404

from .models import Solution


def index(request):
    solutions = get_list_or_404(Solution)
    return render(request, 'portfolio/index.html', {'solutions': solutions})
