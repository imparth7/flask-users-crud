from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    """Initialize the SQLite database."""
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()

# Initialize the database
init_db()

@app.route('/')
def hello():
    return "Hello World"

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required."}), 400

    try:
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            return jsonify({"id": cursor.lastrowid, "name": name, "email": email}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists."}), 400

@app.route('/users', methods=['GET'])
def list_users():
    """List all users."""
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()
        return jsonify([
            {"id": user[0], "name": user[1], "email": user[2]} for user in users
        ])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a single user by ID."""
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        if user:
            return jsonify({"id": user[0], "name": user[1], "email": user[2]})
        else:
            return jsonify({"error": "User not found."}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's details."""
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required."}), 400

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users SET name = ?, email = ? WHERE id = ?
        """, (name, email, user_id))
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found."}), 404
        conn.commit()
        return jsonify({"id": user_id, "name": name, "email": email})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID."""
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found."}), 404
        conn.commit()
        return jsonify({"message": "User deleted successfully."})

if __name__ == '__main__':
    app.run(debug=True)