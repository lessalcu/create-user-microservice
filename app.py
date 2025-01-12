from flask import Flask
from config import Config
from models import db
from routes import create_user

# Create the application
app = Flask(__name__)

# Application configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the create user route
@app.route('/users', methods=['POST'])
def create_user_route():
    return create_user()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)