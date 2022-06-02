from app import app, db
from flask import jsonify, request
from app.api.errors import error_response
from app.models import Player_history, Images
from datetime import date
from flask_login import current_user

@app.route('/api/storestats',methods=['POST'])
def store():
    response = {}
    if not current_user.is_authenticated:
        response['anon'] = "anon"
        return jsonify(response)
    else:
        response['anon'] = 'notanon'
    today = date.today()
    todaydate = today.strftime("%m-%d-%Y")
    data = request.json
    currImg = Images.query.filter_by(date=todaydate)
    username = current_user.username
    ans = data['answer_history']
    count = data['count']
    if data['win'] == "win":
        winstatus = True
    else:
        winstatus =  False
    img_id = currImg
    alreadySubmit = False
    try:
        player = Player_history.query.filter_by(user=username).all()[-1]
        if player.date_submitted == date:
            alreadySubmit = True
    except:
        alreadySubmit = False
    if alreadySubmit:
        return error_response(409, "You've already submitted a score today")
    else:
        submission = Player_history(username,ans,count,img_id,date, winstatus)
        db.session.add(submission)
        db.session.commit()





