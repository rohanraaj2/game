# Import the necessary modules
import os
import sys
from flask import Flask, render_template, request, redirect

# Create a Flask app
app = Flask(__name__)

# Define the routes for the app
@app.route("/")
def index():
    # Get the user's search criteria
    age = request.args.get("age")
    gender = request.args.get("gender")

    # Get a list of users who match the criteria
    users = get_users(age, gender)

    # Render the template with the list of users
    return render_template("index.html", users=users)

@app.route("/profile/<username>")
def profile(username):
    # Get the user's profile
    user = get_user(username)

    # Render the template with the user's profile
    return render_template("profile.html", user=user)

@app.route("/contact")
def contact():
    # Get the user's message
    message = request.args.get("message")

    # Send the message to the admin
    send_message(message)

    # Redirect the user back to the homepage
    return redirect("/")

# Define a function to get a list of users
def get_users(age, gender):
    # Connect to the database
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()

    # Get the list of users who match the criteria
    cursor.execute("SELECT * FROM users WHERE age >= ? AND gender = ?", (age, gender))
    users = cursor.fetchall()

    # Close the connection
    connection.close()

    return users

# Define a function to get a user's profile
def get_user(username):
    # Connect to the database
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()

    # Get the user's profile
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    # Close the connection
    connection.close()

    return user

# Define a function to send a message to the admin
def send_message(message):
    # Connect to the database
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()

    # Insert the message into the database
    cursor.execute("INSERT INTO messages (message) VALUES (?)", (message,))
    connection.commit()

    # Close the connection
    connection.close()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
