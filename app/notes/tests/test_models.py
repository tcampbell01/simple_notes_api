import pytest
from notes.models import Note

# This marks the test as needing database access
@pytest.mark.django_db
class TestNoteModel:
    # Fixture to create a test note
    @pytest.fixture
    def sample_note(self):
        note = Note.objects.create(
            title="Test Note",
            content="This is a test note"
        )
        return note

    def test_create_note(self):
        """Test creating a new note"""
        note = Note.objects.create(
            title="My Note",
            content="My note content"
        )
        assert note.title == "My Note"
        assert note.content == "My note content"

    def test_read_note(self, sample_note):
        """Test reading an existing note"""
        saved_note = Note.objects.get(id=sample_note.id)
        assert saved_note.title == "Test Note"
        assert saved_note.content == "This is a test note"

    def test_update_note(self, sample_note):
        """Test updating a note"""
        sample_note.title = "Updated Title"
        sample_note.save()
        updated_note = Note.objects.get(id=sample_note.id)
        assert updated_note.title == "Updated Title"

    def test_delete_note(self, sample_note):
        """Test deleting a note"""
        note_id = sample_note.id
        sample_note.delete()
        with pytest.raises(Note.DoesNotExist):
            Note.objects.get(id=note_id)



