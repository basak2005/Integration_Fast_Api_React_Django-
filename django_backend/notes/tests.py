from django.test import TestCase
from .models import Note

class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            desc="Test description",
            note="Test content",
            important=True
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.desc, "Test description")
        self.assertEqual(self.note.note, "Test content")
        self.assertTrue(self.note.important)

    def test_note_str(self):
        self.assertEqual(str(self.note), "Test Note")