from django.urls import path,include
from .views import farm_list 
from .views import farm_detail

urlpatterns = [
   
    path('list/',farm_list,name = "farm_list"),
    path('detail/<str:pk>/',farm_detail,name = "farm_detail")
]
