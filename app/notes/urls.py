from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

#This single line automatically creates all these routes for you:

# GET /notes/ - Get all notes

# GET /notes/{id}/ - Get one note

# POST /notes/ - Create a note

# PUT /notes/{id}/ - Update a note completely

# PATCH /notes/{id}/ - Update a note partially

# DELETE /notes/{id}/ - Delete a note

urlpatterns = [
    path('', include(router.urls)),
]
