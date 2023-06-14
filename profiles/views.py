from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import RegistartionSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

@api_view(['POST'])
def register(request):
    serializer = RegistartionSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        data = {}
        token = Token.objects.get(user = user).key
        data['token'] = token
        data['username'] = user.username
        return Response(data)