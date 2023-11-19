from django.urls import path
from .views import index, create_ppt 

urlpatterns = [
    path('create_ppt/', index, name='create_ppt_index'),
    path('create_ppt/api', create_ppt, name='create_ppt_api'),
]