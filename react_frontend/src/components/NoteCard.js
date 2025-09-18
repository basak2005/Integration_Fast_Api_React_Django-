import React, { useState } from 'react';

const NoteCard = ({ note, onEdit, onDelete }) => {
  const [isDeleting, setIsDeleting] = useState(false);

  const handleDelete = async () => {
    if (!window.confirm('Are you sure you want to delete this note?')) {
      return;
    }

    setIsDeleting(true);
    try {
      await onDelete(note.id);
    } catch (error) {
      console.error('Error deleting note:', error);
    } finally {
      setIsDeleting(false);
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className={`note-card ${note.important ? 'important' : ''}`}>
      <div className="note-header">
        <h3 className="note-title">{note.title}</h3>
        {note.important && (
          <span className="important-badge">Important</span>
        )}
      </div>
      
      <p className="note-desc">{note.desc}</p>
      
      <div className="note-content">
        {note.note}
      </div>
      
      <div className="note-meta">
        <small>Created: {formatDate(note.created_at)}</small>
        {note.updated_at !== note.created_at && (
          <small>Updated: {formatDate(note.updated_at)}</small>
        )}
      </div>
      
      <div className="note-actions">
        <button 
          className="btn"
          onClick={() => onEdit(note)}
          disabled={isDeleting}
        >
          Edit
        </button>
        <button 
          className="btn btn-danger"
          onClick={handleDelete}
          disabled={isDeleting}
        >
          {isDeleting ? 'Deleting...' : 'Delete'}
        </button>
      </div>
    </div>
  );
};

export default NoteCard;