import os
import urllib.request
import json
from threading import Thread
import UpdateDB as UDB
import Global as g
from flask import Flask, request, redirect, jsonify
from flask_restful import Resource, Api, reqparse
from werkzeug.utils import secure_filename
from flask import request


# Initialize Flask app and API
app = Flask(__name__)
api = Api(app)

# Set allowed extensions for file upload and upload folder path
ALLOWED_EXTENSIONS = set(['json'])
UPLOAD_FOLDER = '/JSON/'

# Initialize request parser
parser = reqparse.RequestParser()

# Configure upload folder in app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Start a new thread for database update
t1 = Thread(target=UDB.Update)

# Function to check if the uploaded file has allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Resource class for file upload
class Upload(Resource):
    # Start the database update thread
    t1.start()

    # Handle POST request
    def post(self):
        file = request.files['file']
        # If no file is selected for upload, return error message
        if file.filename == '':
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            t1.start()
            return resp

        # If file is selected and has allowed extension, save the file and return success message
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify({'message' : 'File successfully uploaded'})
            resp.status_code = 201
            t1.start()
            return resp
        # If file does not have the allowed extension, return error message
        else:
            resp = jsonify({'message' : 'Allowed file types are only json.'})
            resp.status_code = 400
            return resp
        # curl 127.0.0.1:5000/api -F file=@backup
        
    # Handle DELETE request
    def delete(self):
        try:
            # Try to remove the file and return success message
            os.remove(UPLOAD_FOLDER + 'backup.json')
            resp = jsonify({'message' : 'File successfully deleted'})
            resp.status_code = 201
            t1.start()
            return resp
        except:
            # If file not found, return exception
            return Exception('File not found')
        # curl 127.0.0.1:5000/api -X DELETE

    # Handle GET request
    def get(self):
        with open(UPLOAD_FOLDER + 'backup.json', "r") as json_file:
            # Open the file and return its contents
            data = json.load(json_file)
            return jsonify(data)
        # curl 127.0.0.1:5000/api

class Update(Resource):
    def get(self):
        UDB.Update()
        # creating the necessary arguments for index searching
        parser.add_argument('query', type=int, location='args')
        parser.add_argument('table', type=int, location='args')
        args = parser.parse_args()
        
        # Convert dictionary values to a list and get the list at index args['query']
        try:
            data = list(g.TableDict.values())[args['query']][args['table']]
        # curl 127.0.0.1:5000/api/update?query=0&table=0
        except:
            data = list(g.TableDict.values())[args['query']]
        # curl 127.0.0.1:5000/api/update?query=0
        return jsonify(data)

# Add Upload resource to API
api.add_resource(Upload, '/api')
api.add_resource(Update, '/api/update')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)