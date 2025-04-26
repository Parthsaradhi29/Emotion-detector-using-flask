import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = {"raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = body, headers = headers)
    
    if response.status_code != 200:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None,
               'sadness': None, 'dominant_emotion': None }
    
    formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
    formatted_response['dominant_emotion'] = max(formatted_response, key=formatted_response.get)
    
    return formatted_response
