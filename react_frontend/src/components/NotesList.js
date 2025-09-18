import React from 'react';
import NoteCard from './NoteCard';

const NotesList = ({ notes, loading, onEdit, onDelete }) => {
  if (loading) {
    return <div className="loading">Loading notes...</div>;
  }

  if (!notes || notes.length === 0) {
    return (
      <div className="loading">
        <p>No notes found. Create your first note above!</p>
      </div>
    );
  }

  return (
    <div>
      <h2>Your Notes ({notes.length})</h2>
      <div className="notes-grid">
        {notes.map((note) => (
          <NoteCard
            key={note.id}
            note={note}
            onEdit={onEdit}
            onDelete={onDelete}
          />
        ))}
      </div>
    </div>
  );
};

export default NotesList;