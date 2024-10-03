from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_name.db'
db = SQLAlchemy(app)

# Create tables using app context
with app.app_context():
    db.create_all()

# Define the Pizza model
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name, self.description}"

# Define routes
@app.route('/')
def index():
    return 'Hello!'

@app.route('/pizzas')
def get_pizzas():
    return {"pizzas": "data pizzas"}

# Only wrap operations that require the app context (like db.create_all)
if __name__ == "__main__":
    app.run(debug=True)