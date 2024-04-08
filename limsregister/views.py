from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FarmRegister
from  .serializers import FarmRegisterSerializer

# Create your views here.
@api_view()
def farm_list(request):
    farms = FarmRegister.objects.all()
    serializer = FarmRegisterSerializer(farms,many= True)
    return Response(serializer.data)
