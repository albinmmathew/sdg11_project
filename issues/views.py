from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Issue, Vote, Category
from django.contrib import messages

# Create your views here.
from django.db.models import Case, When, Value, IntegerField

@login_required
def issue_list(request):

    # Main issue list with prioritization
    issues = Issue.objects.select_related('category').annotate(
        emergency_priority=Case(
            When(category__is_emergency=True, then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        )
    ).order_by(
        '-emergency_priority',
        '-votes',
        '-created_at'
    )

    # ✅ SUMMARY COUNTS (THIS IS THE FIX)
    total_count = Issue.objects.count()

    emergency_count = Issue.objects.filter(
        category__is_emergency=True
    ).count()

    resolved_count = Issue.objects.filter(
        status='resolved'
    ).count()

    context = {
        'issues': issues,
        'total_count': total_count,
        'emergency_count': emergency_count,
        'resolved_count': resolved_count,
    }

    return render(request, 'issues/issue_list.html', context)

from .models import Issue, Category

@login_required
def report_issue(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        Issue.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            category=Category.objects.get(id=request.POST.get('category')),
            created_by=request.user
        )
        return redirect('issue_list')

    return render(request, 'issues/report_issue.html', {
        'categories': categories
    })

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


from django.http import JsonResponse

def get_category_info(request):
    category_id = request.GET.get('category_id')

    try:
        category = Category.objects.get(id=category_id)
        return JsonResponse({
            'is_emergency': category.is_emergency,
            'helpline': category.helpline_number
        })
    except Category.DoesNotExist:
        return JsonResponse({
            'is_emergency': False,
            'helpline': ''
        })
