from app import app
from flask import jsonify, url_for, request
from app.api.errors import bad_request,error_response
from app.models import Images
from datetime import datetime,timedelta


@app.route("/api/correctanswer",methods=['GET'])
def correctanswer():
    response = {}
    today=datetime.strftime(datetime.now() - timedelta(0), '%m-%d-%Y')
    image= Images.query.filter_by(date=today).first()
    answer = image.answer
    response['answer'] = answer
    return response
    

