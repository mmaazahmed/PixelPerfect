from app import app,db
from flask import jsonify, url_for, request
from app.api.errors import bad_request,error_response
import json

@app.route("/api/guessattempt",methods=['POST'])
def guessprocessing():
    a = request.get_json(force=True,silent=True)
    data = request.json
    #this will be replaced with a call to the DB and getting the image's metadata
    response = {}
    if data['guess'] == "bmo":
        response['correct'] = "correct"
    else:
        response['correct'] = 'incorrect'
    return jsonify(response)

@app.route("/api/test",methods=["GET"])
def testing():
    response = {}
    response['correct'] = "correct"
    response = jsonify(response)
    return {'a':"test"}


