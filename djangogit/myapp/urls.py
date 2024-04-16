from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('call_time/',views.call_time,name='call_time'),
    path('stop_stream/',views.stop_stream,name='stop_stream'),
]

