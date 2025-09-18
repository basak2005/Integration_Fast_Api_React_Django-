import React, { useState } from 'react';

const NoteForm = ({ onSubmit, initialData = null, onCancel = null }) => {
  const [formData, setFormData] = useState({
    title: initialData?.title || '',
    desc: initialData?.desc || '',
    note: initialData?.note || '',
    important: initialData?.important || false
  });

  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.title.trim() || !formData.desc.trim() || !formData.note.trim()) {
      alert('Please fill in all fields');
      return;
    }

    setIsSubmitting(true);
    try {
      await onSubmit(formData);
      if (!initialData) {
        // Reset form only if creating new note
        setFormData({
          title: '',
          desc: '',
          note: '',
          important: false
        });
      }
    } catch (error) {
      console.error('Error submitting form:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="note-form">
      <h3>{initialData ? 'Edit Note' : 'Create New Note'}</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="title">Title:</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            placeholder="Enter note title"
            disabled={isSubmitting}
          />
        </div>

        <div className="form-group">
          <label htmlFor="desc">Description:</label>
          <input
            type="text"
            id="desc"
            name="desc"
            value={formData.desc}
            onChange={handleChange}
            placeholder="Enter note description"
            disabled={isSubmitting}
          />
        </div>

        <div className="form-group">
          <label htmlFor="note">Content:</label>
          <textarea
            id="note"
            name="note"
            value={formData.note}
            onChange={handleChange}
            placeholder="Enter note content"
            disabled={isSubmitting}
          />
        </div>

        <div className="form-group">
          <div className="checkbox-group">
            <input
              type="checkbox"
              id="important"
              name="important"
              checked={formData.important}
              onChange={handleChange}
              disabled={isSubmitting}
            />
            <label htmlFor="important">Mark as important</label>
          </div>
        </div>

        <div className="note-actions">
          <button 
            type="submit" 
            className="btn btn-success"
            disabled={isSubmitting}
          >
            {isSubmitting ? 'Saving...' : (initialData ? 'Update Note' : 'Create Note')}
          </button>
          
          {onCancel && (
            <button 
              type="button" 
              className="btn"
              onClick={onCancel}
              disabled={isSubmitting}
            >
              Cancel
            </button>
          )}
        </div>
      </form>
    </div>
  );
};

export default NoteForm;