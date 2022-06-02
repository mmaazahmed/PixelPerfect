from app import app, db
from flask import jsonify, url_for, request
from app.api.errors import bad_request, error_response
from app.models import Player_history, Images
from datetime import date
from flask_login import AnonymousUserMixin, current_user

@app.route('/api/storestats',methods=['POST'])
def store():
    today = date.today()
    date = today.strftime("%m/%d/%Y")
    data = request.json
    currImg = Images.query.filter_by(date=date)
    username = current_user.username
    ans = data['answer_history']
    count = data['answer_count']
    winstatus = data['win']
    img_id = currImg
    player = Player_history.query.filter_by(username=username).all()[-1]
    if player.date_submitted == date:
        return error_response(409, "You've already submitted a score today")
    elif (current_user is AnonymousUserMixin):
        return error_response(409, "Anonymous User, score won't be saved")
    else:
        submission = Player_history(username,ans,count,img_id,date)
        db.session.add(submission)
        db.session.commit()





