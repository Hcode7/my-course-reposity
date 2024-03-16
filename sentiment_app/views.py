from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import SentimentModel

# Create your views here.


def sentiment_analysis(request):
    if method == 'POST':
        try:
            data = request.body.decode('utf-8')
            text_to_sentiment = data.get('text', '')
            if text_to_sentiment:
                sentiment_result = sentiment_analyzer(text_to_sentiment)
                SentimentModel.objects.create(
                    text = text_to_sentiment,
                    label = sentiment_result['label'],
                    score = sentiment_result['score']
                )
                # return JsonResponse(sentiment_result)
                return render('sentiment.html', {'sentiment_result' : sentiment_result})
            else:
                return JsonResponse({'message' : 'Text Not Provid'})
        except json.decoder.JSONDecodeError:
            return JsonResponse({'message' : 'Invalid Json'}, status=400)
    else:
        return JsonResponse({'message' : 'Only POST Method Requird'}, status=405)
            


            
def sentiment_analyzer(text_to_sentiment):
    url = 'https://sn-watson-sentiment-cnn.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"rawDocument": {"text", text_to_sentiment}}
    header = {'grpc-metadata-mm-model-id': 'sentiment_aggregated-cnn-workflow_lang_en_stock'}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {'label' : label, 'score' : score}