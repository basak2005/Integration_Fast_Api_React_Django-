from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'important', 'created_at')
    list_filter = ('important', 'created_at')
    search_fields = ('title', 'desc', 'note')
    ordering = ('-created_at',)