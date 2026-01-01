from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Issue, Vote
from django.contrib import messages

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

@login_required
def upvote_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)

    vote, created = Vote.objects.get_or_create(
        user=request.user,
        issue=issue
    )

    if created:
        issue.votes += 1
        issue.save()
    else:
        messages.info(request, "You have already voted for this issue.")

    return redirect('issue_list')

@staff_member_required
def admin_issue_list(request):
    issues = Issue.objects.all().order_by('-votes')
    return render(request, 'issues/admin_issue_list.html', {'issues': issues})

@staff_member_required
def update_status(request, issue_id):
    issue = Issue.objects.get(id=issue_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        issue.status = new_status
        issue.save()

    return redirect('admin_issue_list')
