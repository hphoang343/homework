from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL "/"
@app.route("/")
def hello():
    return "Hello, World!"

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
