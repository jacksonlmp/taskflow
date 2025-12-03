import { useState, useEffect } from 'react';
import { taskService, authService } from '../services/api';
import TaskForm from './TaskForm';
import './TaskList.css';

function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    try {
      setLoading(true);
      const data = await taskService.getTasks();
      setTasks(Array.isArray(data) ? data : data.results || []);
      setError('');
    } catch (err) {
      setError('Failed to load tasks');
      console.error('Error loading tasks:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this task?')) {
      return;
    }

    try {
      await taskService.deleteTask(id);
      setTasks(tasks.filter(task => task.id !== id));
    } catch (err) {
      setError('Failed to delete task');
      console.error('Error deleting task:', err);
    }
  };

  const handleEdit = (task) => {
    setEditingTask(task);
    setShowForm(true);
  };

  const handleFormClose = () => {
    setShowForm(false);
    setEditingTask(null);
  };

  const handleFormSuccess = () => {
    loadTasks();
    handleFormClose();
  };

  const handleLogout = () => {
    authService.logout();
    window.location.reload();
  };

  const toggleTaskStatus = async (task) => {
    try {
      const updatedTask = { ...task, completed: !task.completed };
      await taskService.updateTask(task.id, updatedTask);
      setTasks(tasks.map(t => t.id === task.id ? updatedTask : t));
    } catch (err) {
      setError('Failed to update task');
      console.error('Error updating task:', err);
    }
  };

  return (
    <div className="task-list-container">
      <header className="header">
        <div className="header-content">
          <h1>TaskFlow</h1>
          <button onClick={handleLogout} className="btn-logout">
            Logout
          </button>
        </div>
      </header>

      <main className="main-content">
        <div className="content-wrapper">
          <div className="page-header">
            <div>
              <h2>My Tasks</h2>
              <p className="subtitle">Manage your tasks efficiently</p>
            </div>
            <button 
              onClick={() => setShowForm(true)} 
              className="btn-primary"
            >
              + New Task
            </button>
          </div>

          {error && (
            <div className="error-banner">
              {error}
              <button onClick={() => setError('')} className="close-btn">×</button>
            </div>
          )}

          {loading ? (
            <div className="loading">Loading tasks...</div>
          ) : tasks.length === 0 ? (
            <div className="empty-state">
              <h3>No tasks yet</h3>
              <p>Create your first task to get started!</p>
              <button onClick={() => setShowForm(true)} className="btn-primary">
                Create Task
              </button>
            </div>
          ) : (
            <div className="tasks-grid">
              {tasks.map(task => (
                <div key={task.id} className={`task-card ${task.completed ? 'completed' : ''}`}>
                  <div className="task-header">
                    <input
                      type="checkbox"
                      checked={task.completed}
                      onChange={() => toggleTaskStatus(task)}
                      className="task-checkbox"
                    />
                    <h3 className="task-title">{task.title}</h3>
                  </div>
                  
                  {task.description && (
                    <p className="task-description">{task.description}</p>
                  )}
                  
                  <div className="task-footer">
                    <span className="task-date">
                      {new Date(task.created_at).toLocaleDateString()}
                    </span>
                    <div className="task-actions">
                      <button 
                        onClick={() => handleEdit(task)}
                        className="btn-edit"
                        title="Edit"
                      >
                        ✏️
                      </button>
                      <button 
                        onClick={() => handleDelete(task.id)}
                        className="btn-delete"
                        title="Delete"
                      >
                        🗑️
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </main>

      {showForm && (
        <TaskForm
          task={editingTask}
          onClose={handleFormClose}
          onSuccess={handleFormSuccess}
        />
      )}
    </div>
  );
}

export default TaskList;
