from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} , {self.description}"


def index():
    return 'Hello!'


@app.route('/pizza')
def get_pizza():
    return {"pizza": "pizza data"}


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
