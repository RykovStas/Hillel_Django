from django.contrib import admin

from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    search = ('path',)
    list_display = ('path', 'method', 'timestamp', )
    list_filter = ('timestamp', 'method', )
    list_editable = ('method',)
    ordering = ('-timestamp',)
