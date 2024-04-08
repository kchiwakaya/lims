from django.urls import path,include
from .views import farm_list 
urlpatterns = [
   
    path('list/',farm_list,name = "farm_list")
]
