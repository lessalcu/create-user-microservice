from flask import Flask
from flask_cors import CORS
from src.config.config import Config
from src.models.models import db
from src.routes.routes import create_user

# Create the application
app = Flask(__name__)

# Enable CORS
CORS(app)

# Application configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the create user route
@app.route('/users', methods=['POST'])
def create_user_route():
    return create_user()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
