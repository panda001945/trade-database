from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Database configuration
DATABASE = 'trade.db'


# Initialize the database
def init_db():
    if not os.path.exists(DATABASE):  # Only create if database does not exist
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS trades (
                    serial_number INTEGER PRIMARY KEY AUTOINCREMENT,
                    currency_pair TEXT NOT NULL,
                    date TEXT NOT NULL,
                    buy_sell TEXT NOT NULL,
                    type_of_trade TEXT NOT NULL,
                    link_to_trade TEXT
                )
            """)
        print("Database initialized.")


# Routes
@app.route('/')
def index():
    # Fetch all trades from the database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trades")
        trades = cursor.fetchall()
    return render_template('index.html', trades=trades)


@app.route('/add', methods=['GET', 'POST'])
def add_trade():
    if request.method == 'POST':
        # Get data from form submission
        data = request.form
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO trades (currency_pair, date, buy_sell, type_of_trade, link_to_trade)
                VALUES (?, ?, ?, ?, ?)
            """, (data['currency_pair'], data['date'], data['buy_sell'], data['type_of_trade'], data['link_to_trade']))
        return redirect(url_for('success'))
    return render_template('add_trade.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/delete/<int:serial_number>', methods=['POST'])
def delete_trade(serial_number):
    # Delete trade by its serial_number
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM trades WHERE serial_number = ?", (serial_number,))
    return redirect(url_for('index'))


# Start the app
if __name__ == '__main__':
    init_db()  # Ensure database is initialized
    app.run(debug=True)
