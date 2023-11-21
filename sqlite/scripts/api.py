import os
import urllib.request
import json
import UpdateDB as UDB
import Global as g
from flask import Flask, request, redirect, jsonify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

g.api = True

app = Flask(__name__)
api = Api(app)

ALLOWED_EXTENSIONS = set(['json'])
UPLOAD_FOLDER = 'X:/sqlite/JSON/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Upload(Resource):
    
    def post(self):
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            UDP.Update()
            return resp
            
        else:
            resp = jsonify({'message' : 'Allowed file types are only json.'})
            resp.status_code = 400
            return resp
        # curl 127.0.0.1:5000/api -F file=@backup
        
    def delete(self):
        try:
            os.remove(UPLOAD_FOLDER + 'backup.json')
            resp = jsonify({'message' : 'File successfully deleted'})
            resp.status_code = 201
            return resp
        except:
            return Exception('File not found')
        # curl 127.0.0.1:5000/api -X DELETE
        
    def get(self):
        with open(UPLOAD_FOLDER + 'backup.json', "r") as json_file:
            x = json.load(json_file)
            resp = jsonify(x)
            resp.status_code = 201
            return resp
        # curl 127.0.0.1:5000/api

api.add_resource(Upload, '/api')

if __name__ == "__main__":
    app.run(debug=True)