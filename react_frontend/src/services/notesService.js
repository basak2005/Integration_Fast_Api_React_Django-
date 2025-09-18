import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/integration';

class NotesService {
  constructor() {
    this.api = axios.create({
      baseURL: API_BASE_URL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  // Get all notes
  async getAllNotes() {
    try {
      const response = await this.api.get('/notes');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch notes: ${error.response?.data?.detail || error.message}`);
    }
  }

  // Get single note
  async getNote(id) {
    try {
      const response = await this.api.get(`/notes/${id}`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch note: ${error.response?.data?.detail || error.message}`);
    }
  }

  // Create new note
  async createNote(noteData) {
    try {
      const response = await this.api.post('/notes', noteData);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to create note: ${error.response?.data?.detail || error.message}`);
    }
  }

  // Update note
  async updateNote(id, noteData) {
    try {
      const response = await this.api.put(`/notes/${id}`, noteData);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to update note: ${error.response?.data?.detail || error.message}`);
    }
  }

  // Delete note
  async deleteNote(id) {
    try {
      const response = await this.api.delete(`/notes/${id}`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to delete note: ${error.response?.data?.detail || error.message}`);
    }
  }

  // Health check
  async healthCheck() {
    try {
      const response = await this.api.get('/health');
      return response.data;
    } catch (error) {
      throw new Error(`Health check failed: ${error.response?.data?.detail || error.message}`);
    }
  }
}

export default new NotesService();