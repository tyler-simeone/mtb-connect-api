import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from mtbconnectapi.models import User as WebUser

@csrf_exempt
def register_user(request):


    req_body = json.loads(request.body.decode())

  
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    web_user = WebUser.objects.create(
        user=new_user,
        avatar_img=req_body["avatar_img"]
        )


    web_user.save()

 
    token = Token.objects.create(user=new_user)

    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')