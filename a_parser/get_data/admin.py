from django.contrib import admin

from .models import LogsModel

@admin.register(LogsModel)
class LogsModel(admin.ModelAdmin):
    list_display = ('ip', 'date')
    list_filter = ('method', 'response')

    search_fields = ('ip__startswith', 'date__startswith')