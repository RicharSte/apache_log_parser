from django.contrib import admin

from .models import LogsModel

@admin.register(LogsModel) #
class LogsModel(admin.ModelAdmin):
    list_display = ('ip', 'date') #выводим в админке все запросы по ip и дате
    list_filter = ('method', 'response') #добавляем фильтры для впоиска в админке

    search_fields = ('ip__startswith', 'date__startswith') #добавляем поиск по ip или дате