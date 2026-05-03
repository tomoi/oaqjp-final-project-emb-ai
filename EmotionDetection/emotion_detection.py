import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)

    dominant_score = 0

    for key, value in formatted_response["emotionPredictions"][0]["emotion"].items():

        if value > dominant_score:
            dominant_score = value
            dominant_emotion = key 

    final_response = formatted_response["emotionPredictions"][0]["emotion"]
    final_response["dominant_emotion"] = dominant_emotion

    return final_response