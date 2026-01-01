from django.contrib import admin
from .models import Issue, Vote, Category

# Register your models here.

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'status', 'votes', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'location')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'issue')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_emergency', 'helpline_number')
    list_filter = ('is_emergency',)
