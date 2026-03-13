from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2.extras import RealDictCursor
import os
import time

app = Flask(__name__)

# DB config from env vars
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'postgres'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'password')
}

def get_db_connection(max_retries=5):
    """Get database connection with retry logic"""
    retries = 0
    while retries < max_retries:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            return conn
        except psycopg2.OperationalError as e:
            retries += 1
            if retries == max_retries:
                print(f"Failed to connect to database after {max_retries} attempts: {e}")
                raise
            print(f"Database connection attempt {retries} failed, retrying in 5 seconds...")
            time.sleep(5)

def init_db():
    """Initialize database tables"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")
        # Don't raise - allow app to continue and retry on requests

@app.route('/health')
def health():
    """Health check endpoint for ALB"""
    try:
        # Try to connect to database
        conn = get_db_connection()
        conn.close()
        return {'status': 'healthy', 'database': 'connected'}, 200
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}, 500

@app.route('/')
def index():
    try:
        init_db()  # This will retry if needed
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM tasks ORDER BY created_at DESC')
        tasks = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', tasks=tasks)
    except Exception as e:
        return f"Database error: {str(e)}", 500

@app.route('/add', methods=['POST'])
def add_task():
    try:
        init_db()
        title = request.form['title']
        description = request.form.get('description', '')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO tasks (title, description) VALUES (%s, %s)', (title, description))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error adding task: {str(e)}", 500

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    try:
        init_db()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE tasks SET completed = TRUE WHERE id = %s', (task_id,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error completing task: {str(e)}", 500

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    try:
        init_db()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error deleting task: {str(e)}", 500

if __name__ == '__main__':
    # Run init_db on startup
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)