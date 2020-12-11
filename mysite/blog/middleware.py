from django.http import HttpResponse
import time
import json


import time
import datetime

class RequestMiddleware:
   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):
       timestamp = time.monotonic()

       # log_time = datetime.datetime.now()

       response = self.get_response(request)

       print(
           f'Продолжительность запроса {request.path} - '
           f'{time.monotonic() - timestamp:.3f} сек.'
       )

       data = {
           # 'time': log_time,
           'path': request.path,
       }

       with open('request.log', 'a') as f:
           f.write(json.dumps(data) + '\n')

       return response
