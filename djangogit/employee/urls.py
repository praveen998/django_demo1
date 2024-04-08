from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),  
    path('show/',views.show,name='show'),
    path('emp/',views.emp,name='emp'),
    path('myview/',views.myview,name='myview'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]
