from django.shortcuts import render, get_list_or_404

from .models import Solution


def index(request):
    solutions = get_list_or_404(Solution.objects.order_by('-featured', '-release_date'))
    return render(request, 'portfolio/index.html', {'solutions': solutions})
