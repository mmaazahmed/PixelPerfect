from app import app 
from flask import jsonify
from app.models import Player_history
from flask_login import current_user

@app.route('/api/getUserStats',methods=['GET'])
def getStats():
    response = {}
    if not current_user.is_authenticated:
        response['currStreak'] = "anonymous"
        return jsonify(response)
    username =  current_user.user
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
    response['currStreak'] = currStreak
    response['highestStreak'] = finalHighest
    for i in range(5):
        response[i+1] = dist[i] 
    return jsonify(response)



        
    
