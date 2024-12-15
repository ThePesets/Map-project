from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('info1', views.info1, name='full_info1'),
    path('info2', views.info2, name='full_info2'),
]
