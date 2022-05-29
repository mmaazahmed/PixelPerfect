from app import app, db
from flask import jsonify, url_for, request
from app.api.errors import bad_request, error_response
from app.models import Player_history
from datetime import date
from flask_login import AnonymousUserMixin, current_user

app.route('/api/getUserStats',methods=['POST'])
def getStats():
    username =  current_user.username
    records = Player_history.query.filter_by(username=username).all()
    revRec = records.reverse()
    currStreak = 0
    dist = [0,0,0,0,0]
    #currStreak
    for i in revRec:
        if i.win == 0:
            break
        else:
            currStreak += 1
    highestStreak = 0
    streaks = []
    for i in records:
        if i.win == 1:
            dist[i.count] += 1
            highestStreak += 1
        else:
            streaks.append(highestStreak)
            highestStreak = 0
    finalHighest = max(streaks)
    response = {}
    response['currStreak'] = currStreak
    response['highestStreak'] = finalHighest
    for i in range(5):
        response[i+1] = dist[i] 
    return jsonify(response)



        
    
