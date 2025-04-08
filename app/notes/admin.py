from django.contrib import admin
from .models import Note, Usuario

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  
    search_fields = ('title', 'content')  
    list_filter = ('created_at', 'updated_at')  

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  
