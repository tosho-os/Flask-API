from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)



@app.route('/get')
def get_task():
       # Fetch tasks after possible insert
    conn = sqlite3.connect('Simple_API/database.db')
    conn.row_factory = sqlite3.Row
    connection = conn.cursor()
    connection.execute('SELECT id, task, is_done FROM todo')
    tasks = connection.fetchall()
    conn.close()

    return jsonify([{"id": row["id"], "task": row["task"], "is_done": row["is_done"]} for row in tasks]),200

@app.route('/add', methods = ['POST'])
def add_task():
    data = request.get_json() 
    new_task = data['task']

    conn = sqlite3.connect('Simple_API/database.db')
    connection = conn.cursor()
    connection.execute('INSERT INTO todo (task, is_done) VALUES (?,0)', (new_task,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"}), 201

@app.route('/delete', methods=["POST"])
def delete_task():
    data = request.get_json()
    task_id = data['id']
    conn = sqlite3.connect('Simple_API/database.db')
    connection = conn.cursor()
    connection.execute('DELETE FROM todo WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Deletion successfully"}), 201

@app.route('/done', methods=["POST"])
def done():
    data = request.get_json()
    task_id = data['id']
    conn = sqlite3.connect('Simple_API/database.db')
    connection = conn.cursor()
    connection.execute('UPDATE todo SET is_done = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Marked done successfully"}), 201

if __name__ == '__main__':
   app.run(debug=True)