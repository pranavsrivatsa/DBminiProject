from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Staff(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128))
    Age = db.Column(db.Integer)
    Salary = db.Column(db.DECIMAL(10,5))
    Work = db.Column(db.String(128))

class Account(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(128))
    Password = db.Column(db.String(128))


if __name__ == '__main__':
    manager.run()
