import requests
import json


def push_alert():
    reqUrl = "http://127.0.0.1:5000/api/v1/alerts"

    headersList = {"Accept": "*/*", "Content-Type": "application/json"}

    payload = json.dumps({"bus_id": 521415, "category": "pose_detection"})

    response = requests.request("POST", reqUrl, data=payload, headers=headersList)

    print(response.text)
