import pytest
from rest_framework.test import APIClient
from notes.models import Note

@pytest.mark.django_db
class TestNoteAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def sample_note(self):
        note = Note.objects.create(
            title="Test Note",
            content="This is a test note"
        )
        return note

    def test_list_notes(self, api_client):
        """Test getting list of notes"""
        response = api_client.get('/api/notes/')
        assert response.status_code == 200

    def test_create_note(self, api_client):
        """Test creating a new note"""
        data = {
            "title": "New Note",
            "content": "New content"
        }
        response = api_client.post('/api/notes/', data)
        assert response.status_code == 201
        assert response.data['title'] == "New Note"
        assert response.data['content'] == "New content"

    def test_get_note_detail(self, api_client, sample_note):
        """Test getting a single note"""
        response = api_client.get(f'/api/notes/{sample_note.id}/')
        assert response.status_code == 200
        assert response.data['title'] == "Test Note"

    def test_update_note(self, api_client, sample_note):
        """Test updating a note"""
        data = {"title": "Updated Title"}
        response = api_client.patch(
            f'/api/notes/{sample_note.id}/',
            data,
            format='json'
        )
        assert response.status_code == 200
        assert response.data['title'] == "Updated Title"

    def test_delete_note(self, api_client, sample_note):
        """Test deleting a note"""
        response = api_client.delete(f'/api/notes/{sample_note.id}/')
        assert response.status_code == 204
        assert not Note.objects.filter(id=sample_note.id).exists()
