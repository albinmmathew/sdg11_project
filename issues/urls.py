from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue_list, name='issue_list'),
    path('report/', views.report_issue, name='report_issue'),
	path('upvote/<int:issue_id>/', views.upvote_issue, name='upvote_issue'),
	path('admin/', views.admin_issue_list, name='admin_issue_list'),
	path('admin/update/<int:issue_id>/', views.update_status, name='update_status'),
	path('ajax/category-info/', views.get_category_info, name='category_info'),
	
]
