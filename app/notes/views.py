from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

#If you want to override the default behavior of the ModelViewSet, you can create your own viewset class that inherits from the ModelViewSet and overrides the necessary methods. Here's an example of how you can do that:

# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def list(self, request):
#         # Custom code for getting all notes
#         return super().list(request)

#     def create(self, request):
#         # Custom code for creating a note
#         return super().create(request)
