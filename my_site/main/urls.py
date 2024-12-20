from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('info1', views.info1, name='full_info1'),
    path('info2', views.info2, name='full_info2'),
    path('info3', views.info3, name='full_info3'),
    path('info4', views.info4, name='full_info4'),
    path('info5', views.info5, name='full_info5'),
    path('info6', views.info6, name='full_info6'),
    path('info7', views.info7, name='full_info7'),
    path('info8', views.info8, name='full_info8'),
    path('info9', views.info9, name='full_info9'),
    path('info10', views.info10, name='full_info10'),
    path('info11', views.info11, name='full_info11'),
    path('info12', views.info12, name='full_info12'),
    path('info13', views.info13, name='full_info13'),
    path('info14', views.info14, name='full_info14'),
    path('info15', views.info15, name='full_info15'),
    path('info16', views.info16, name='full_info16'),
    path('info17', views.info17, name='full_info17'),
    path('info18', views.info18, name='full_info18'),
]
