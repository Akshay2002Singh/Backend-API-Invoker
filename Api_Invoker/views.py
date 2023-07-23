import requests,json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt    
def call(request):
    if request.method == 'POST':
        try:
            # get body of request
            body = json.loads(request.body)
            # get api parameter from body 
            api = body['api']
            # make request on api 
            x = requests.get(api)
            # convert data from json to python object
            x = json.loads(x.text)
            # return as json 
            return JsonResponse(x)
        except:
            return JsonResponse({
                "message" : "request does not contain api parameter or api is invalid",
            })

    return JsonResponse({
        "message" : "request must be post",
    })