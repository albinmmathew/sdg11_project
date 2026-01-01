from django.contrib import admin
from .models import Issue

# Register your models here.

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'status', 'votes', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'location')
