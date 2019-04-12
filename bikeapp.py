import requests
import json
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)


def get_request():
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')

    if action == "get_bike":
        obj = requests.get('https://feeds.citibikenyc.com/stations/stations.json')
        res = obj.json()
        JayStDock = res['stationBeanList'][175]['availableDocks']
        ClarkStBike = res['stationBeanList'][174]['availableBikes']
        result = {'fulfillmentText': 'Jay street has ' + str(JayStDock) + ' docks and Clark street has ' + str(ClarkStBike) + ' bikes'}
        return jsonify(result)

@app.route("/webhook", methods=['GET','POST'])
def index():
    return get_request()

@app.route("/")
def hello():
    return "Bike App"

if __name__ == "__main__":
    app.run("127.0.0.1", debug=True)
