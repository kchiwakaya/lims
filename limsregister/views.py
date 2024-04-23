from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FarmRegister
from  .serializers import FarmRegisterSerializer

# Create your views here.
@api_view(["POST","GET"])
def farm_list(request):
    if request.method == "POST":
        serializer = FarmRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "GET": 
        farms = FarmRegister.objects.all()
        serializer = FarmRegisterSerializer(farms,many= True)
        return Response(serializer.data)
@api_view(["GET","PUT","DELETE"])
def farm_detail(request,pk):
    if request.method == "GET":
        farm = FarmRegister.objects.get(pk=pk)
        serializer = FarmRegisterSerializer(farm)
        return Response(serializer.data)
    elif request.method == "PUT":
        farm = FarmRegister.objects.get(pk=pk)
        serializer = FarmRegisterSerializer(farm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        farm = FarmRegister.objects.get(pk=pk)
        farm.delete()
        return Response("deleted")