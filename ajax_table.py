from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # url for creating db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # connecting app to db


class User(db.Model):  # user entity in db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))

    def to_dict(self):  # method that can return a user as a Python dictionary that can be serialized to JSON
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }


db.create_all()  # adding table to db


@app.route('/')  # main page
def index():
    return render_template('ajax_table.html', title='Ajax Table')


@app.route('/api/data')  # second end-point to return a JSON payload
def data():
    return {'data': [user.to_dict() for user in User.query]}


if __name__ == '__main__':
    app.run()
