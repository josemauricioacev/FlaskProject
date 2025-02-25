from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="db"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")  # Asegúrate de que la tabla 'students' existe
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)