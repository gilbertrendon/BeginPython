from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World'

@app.route('/add_contact')
def add_contact():
    return 'add_contact'

@app.route('/edit_contact')
def edit_contact():
    return 'add_contact'

@app.route('/delete_contact')
def delete_contact():
    return 'delete_contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
