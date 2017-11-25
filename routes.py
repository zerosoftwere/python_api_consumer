from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)
API = 'http://localhost:5000/'

@app.route('/', methods=['GET'])
def index():
    result = requests.get(API + 'api/images')
    images = result.json()
    return render_template('index.html', images=images)

@app.route('/', methods=['POST'])
def insert():
    description = request.form['description']
    file = request.files['file']

    data = {'description': description}
    files = {'file': (file.filename, file.stream, file.mimetype)}
    
    result = requests.post(API + 'api/images', 
        data=data, files=files)
    return redirect('/')

@app.route('/<int:id>', methods=['GET'])
def retrive(id):
    result = requests.get(API + 'api/images/%d' % id);
    return redirect(API + result.json()['path'])

application = app
if __name__ == '__main__':
    application.run(debug=True, port=8000)
