import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework import status


from django.shortcuts import render
from . import service

def get_req_body_json(request):
    try:
        return json.loads(request.body)
    except Exception as e:
        print("exception is", e)
    return None

def get_animals_data(request):
    resp = service.get_questions()
    formatted_resp = resp
    resp_msg = {
        "questions": formatted_resp,
        "status": status.HTTP_200_OK
    }
    return JsonResponse(resp_msg)


def validate_animals_response(request):
    req_body = get_req_body_json(request)
    responses = req_body.get('responses')
    print("responses => ", responses)
    identifier = service.identify_animal(responses)
    resp_msg = {
        "identifier": identifier,
        "status": status.HTTP_200_OK
    }
    return JsonResponse(resp_msg)
