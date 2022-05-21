from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:hydrocarbons@localhost:5432/alx'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()
    # db.session.commit()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
