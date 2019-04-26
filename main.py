import requests
import json
from flask import Flask, make_response, request, jsonify, render_template

app = Flask(__name__)

def get_request():
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    
    if action == "get_bike":
        obj = requests.get('https://feeds.citibikenyc.com/stations/stations.json')
        res = obj.json()
        JayStDock = res['stationBeanList'][155]['availableDocks']
        ClarkStBike = res['stationBeanList'][154]['availableBikes']
        result = {'fulfillmentText': 'Jay street has ' + str(JayStDock) + ' docks and Clark street has ' + str(ClarkStBike) + ' bikes'}
        return jsonify(result)

@app.route("/webhook", methods=['GET','POST'])
def index():
    return get_request()

@app.route("/")
def hello():
    obj = requests.get('https://feeds.citibikenyc.com/stations/stations.json')
    res = obj.json()
    stationNameJay = res['stationBeanList'][155]['stationName']
    stationNameClark = res['stationBeanList'][154]['stationName']
    IDClark = res['stationBeanList'][154]['id']
    IDJay = res['stationBeanList'][155]['id']
    

    return render_template('index.html', stationNameJay = stationNameJay, stationNameClark = stationNameClark, IDClark = IDClark, IDJay = IDJay)

if __name__ == "__main__":
    app.run("127.0.0.1", debug=True, port=8080)
