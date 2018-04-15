from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<int:tag_id>/', views.index, name='filtered_index'),
    path('solution/<int:solution_id>/', views.solution_detail, name='solution_detail')
]
