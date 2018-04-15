from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Solution, Tag


def index(request):
    solutions = get_list_or_404(Solution.objects.order_by('-featured', 'description_only', '-release_date'))
    tags = get_list_or_404(Tag)
    return render(request, 'portfolio/index.html', {'solutions': solutions, 'tags': tags})


def solution_detail(request, solution_id):
    solution = get_object_or_404(Solution.objects.exclude(description_only=True), pk=solution_id)
    return render(request, 'portfolio/solution_detail.html', {'solution': solution})
