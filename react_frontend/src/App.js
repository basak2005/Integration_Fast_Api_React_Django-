import React, { useState, useEffect } from 'react';
import './App.css';
import NoteForm from './components/NoteForm';
import NotesList from './components/NotesList';
import notesService from './services/notesService';

function App() {
  const [notes, setNotes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const [editingNote, setEditingNote] = useState(null);
  const [healthStatus, setHealthStatus] = useState(null);

  useEffect(() => {
    loadNotes();
    checkHealth();
  }, []);

  const checkHealth = async () => {
    try {
      const health = await notesService.healthCheck();
      setHealthStatus(health);
    } catch (error) {
      console.error('Health check failed:', error);
      setHealthStatus({ 
        fastapi_status: 'disconnected', 
        django_backend_status: 'disconnected',
        message: 'Connection failed'
      });
    }
  };

  const loadNotes = async () => {
    try {
      setLoading(true);
      setError(null);
      const fetchedNotes = await notesService.getAllNotes();
      setNotes(fetchedNotes);
    } catch (error) {
      setError(error.message);
      console.error('Error loading notes:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateNote = async (noteData) => {
    try {
      setError(null);
      const newNote = await notesService.createNote(noteData);
      setNotes(prev => [newNote, ...prev]);
      setSuccess('Note created successfully!');
      setTimeout(() => setSuccess(null), 3000);
    } catch (error) {
      setError(error.message);
      throw error;
    }
  };

  const handleUpdateNote = async (noteData) => {
    try {
      setError(null);
      const updatedNote = await notesService.updateNote(editingNote.id, noteData);
      setNotes(prev => prev.map(note => 
        note.id === editingNote.id ? updatedNote : note
      ));
      setEditingNote(null);
      setSuccess('Note updated successfully!');
      setTimeout(() => setSuccess(null), 3000);
    } catch (error) {
      setError(error.message);
      throw error;
    }
  };

  const handleEditNote = (note) => {
    setEditingNote(note);
    setError(null);
  };

  const handleCancelEdit = () => {
    setEditingNote(null);
    setError(null);
  };

  const handleDeleteNote = async (noteId) => {
    try {
      setError(null);
      await notesService.deleteNote(noteId);
      setNotes(prev => prev.filter(note => note.id !== noteId));
      setSuccess('Note deleted successfully!');
      setTimeout(() => setSuccess(null), 3000);
    } catch (error) {
      setError(error.message);
      throw error;
    }
  };

  return (
    <div className="App">
      <div className="container">
        <div className="header">
          <h1>📝 Notes App</h1>
          <p>React Frontend → FastAPI Integration → Django Backend</p>
          {healthStatus && (
            <div className="health-status">
              <small>
                FastAPI: {healthStatus.fastapi_status} | 
                Django: {healthStatus.django_backend_status}
              </small>
            </div>
          )}
        </div>

        {error && (
          <div className="error">
            <strong>Error:</strong> {error}
          </div>
        )}

        {success && (
          <div className="success">
            <strong>Success:</strong> {success}
          </div>
        )}

        <NoteForm
          onSubmit={editingNote ? handleUpdateNote : handleCreateNote}
          initialData={editingNote}
          onCancel={editingNote ? handleCancelEdit : null}
        />

        <NotesList
          notes={notes}
          loading={loading}
          onEdit={handleEditNote}
          onDelete={handleDeleteNote}
        />
      </div>
    </div>
  );
}

export default App;