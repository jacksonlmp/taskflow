import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

export const authService = {
  login: async (username, password) => {
    const response = await api.post('/api/auth/login/', { username, password });
    if (response.data.token) {
      localStorage.setItem('token', response.data.token);
    }
    return response.data;
  },
  
  logout: () => {
    localStorage.removeItem('token');
  },
  
  isAuthenticated: () => {
    return !!localStorage.getItem('token');
  },
};

export const taskService = {
  getTasks: async () => {
    const response = await api.get('/api/tasks/');
    return response.data;
  },
  
  getTask: async (id) => {
    const response = await api.get(`/api/tasks/${id}/`);
    return response.data;
  },
  
  createTask: async (task) => {
    const response = await api.post('/api/tasks/', task);
    return response.data;
  },
  
  updateTask: async (id, task) => {
    const response = await api.put(`/api/tasks/${id}/`, task);
    return response.data;
  },
  
  deleteTask: async (id) => {
    await api.delete(`/api/tasks/${id}/`);
  },
};

export default api;
