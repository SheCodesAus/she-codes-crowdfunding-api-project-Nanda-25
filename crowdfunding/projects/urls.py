from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),
    path('projects/filter', views.ProjectListFilter.as_view(), name="project-list-filter"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(),name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name="pledge-list"),
    path('projects/<int:pk>/bookmarked/', views.LikeListCreate.as_view(), name='project-bookmarked'),
]

urlpatterns = format_suffix_patterns(urlpatterns)