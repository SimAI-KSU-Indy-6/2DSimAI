from flask import Flask, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

# Database Connection Function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="team_user",
        password="indy6",
        database="agent_simulation",
        auth_plugin='mysql_native_password'
    )

# Fix: Convert timedelta to a string before sending JSON response
def serialize_thoughts(rows):
    for row in rows:
        for key, value in row.items():
            if isinstance(value, datetime.timedelta):  # Convert timedelta to string
                row[key] = str(value)
    return rows

# Route to Retrieve Thoughts (GET)
@app.route('/thoughts', methods=['GET'])
def get_thoughts():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM thoughts ORDER BY date DESC, time DESC LIMIT 10")
    thoughts = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(serialize_thoughts(thoughts))  # Converts timedelta to string

# ✅ Route to Store a Thought (POST)
@app.route('/add_thought', methods=['POST'])
def add_thought():
    try:
        data = request.json  # Get JSON data sent from the simulation
        db = get_db_connection()
        cursor = db.cursor()

        sql = """INSERT INTO thoughts (date, time, start_location, thought, action, target_location, target_location_description, end_location)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (
            data['date'],
            data['time'],
            data['start_location'],
            data['thought'],
            data['action_description'],
            data['target_location'],
            data['target_location_description'],
            data['target_coordinates']
        )

        cursor.execute(sql, values)
        db.commit()

        cursor.close()
        db.close()

        return jsonify({"message": "Thought added successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors properly

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
