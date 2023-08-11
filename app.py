from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Using SQLite database
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(255))
    field2 = db.Column(db.String(255))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        field1 = request.form['field1']
        field2 = request.form['field2']
        entry = Entry(field1=field1, field2=field2)
        db.session.add(entry)
        db.session.commit()

    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)