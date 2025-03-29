from django.contrib import admin
from .models import Usuario, Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # columns to show in list view
    search_fields = ('title', 'content')  # fields to search by
    list_filter = ('created_at', 'updated_at')  # filters on the right side

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # adjust fields based on your Usuario model
