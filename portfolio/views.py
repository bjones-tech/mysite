from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Solution, Tag


def index(request, tag_id=0):
    if tag_id:
        solutions = get_list_or_404(Tag.objects.get(pk=tag_id).solution_set)
    else:
        solutions = get_list_or_404(Solution)

    tags = get_list_or_404(Tag)

    return render(request, 'portfolio/index.html', {'solutions': solutions, 'tags': tags, 'tag_id': tag_id})


def solution_detail(request, solution_id):
    solution = get_object_or_404(Solution.objects.exclude(description_only=True), pk=solution_id)

    return render(request, 'portfolio/solution_detail.html', {'solution': solution})
