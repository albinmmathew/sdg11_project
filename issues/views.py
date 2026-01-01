from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Issue

# Create your views here.
@login_required
def issue_list(request):
    issues = Issue.objects.all().order_by('-votes', '-created_at')
    return render(request, 'issues/issue_list.html', {'issues': issues})

@login_required
def report_issue(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')

        Issue.objects.create(
            title=title,
            description=description,
            location=location,
            created_by=request.user
        )
        return redirect('issue_list')

    return render(request, 'issues/report_issue.html')
