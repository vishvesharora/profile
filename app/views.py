
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile



@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def create(request):
    profile_data = Profile.objects.filter(user = request.user).exists()
    if profile_data:
        return Response({
            'message': "Your Profile already exist"
        })
    serializer = ProfileSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        profile = serializer.save(user = request.user)
        return Response({
            'message': "Profile created succesfully"
        })

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])    
def update(request):
    try:
        profile_data = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        return Response({
            'message': "Profile does not exist"
        })
    
    serializer = ProfileSerializer(profile_data, data = request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        profile = serializer.save()
        return Response({
            'message': "Profile updated succesfully"
        })

