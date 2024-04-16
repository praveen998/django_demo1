from django.shortcuts import render
from django.http import StreamingHttpResponse   
from django.http import HttpResponse   
from datetime import datetime  
from django.http import JsonResponse
import time

flag=1
# Create your views here.
def index(request):
    return render(request,'index.html',{'name':'praveen'})

def call_time(request):
    stop_stream = False
    def event_stream():
        while not stop_stream:
            current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield f'data: {current_time}\n\n'    
            time.sleep(1)

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    return response
    
def stop_stream(request):
    global stop_stream
    stop_stream=True
    return HttpResponse('streaming stoped')