from django.urls import path
from .views import NoteListCreateView, NoteDetailView

urlpatterns = [
    # Route for listing and creating notes
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    
    # Route for retrieving, updating, and deleting a single note
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]