from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue_list, name='issue_list'),
    path('report/', views.report_issue, name='report_issue'),
]
