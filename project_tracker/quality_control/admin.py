from django.contrib import admin
from .models import Bug_Report,FeatureRequest
# Register your models here.
class Bug_ReportInline(admin.TabularInline):
    model = Bug_Report
    extra = 0
    fields = ('task', 'description', 'assignee', 'priority', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True
@admin.register(Bug_Report)
class Bug_ReportAdmin(admin.ModelAdmin):
    list_display = ('task', 'project', 'assignee', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'assignee', 'project','priority')
    search_fields = ('task', 'description')
    list_editable = ('status', 'assignee')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('task', 'project', 'assignee', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'assignee', 'project')
    search_fields = ('task', 'description')
    list_editable = ('status', 'assignee')
    readonly_fields = ('created_at', 'updated_at')
