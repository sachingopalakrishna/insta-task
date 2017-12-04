from django.shortcuts import render
from .models import InstaUser
from .serializers import InstaUserSerializer, InstaUserEditSerializer
from django.http.response import JsonResponse
from rest_framework.views import APIView
from annoying.functions import get_object_or_None

class InstaUserAddList(APIView):
    """
    to add new user and list all
    """
    def post(self, request):
        serializer = InstaUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'user': serializer.data}, status=201)
        else:
            print (serializer.errors)
            return JsonResponse({'message': serializer.errors}, status=400)

    def get(self, request):
        users = InstaUser.objects.all()
        serializer = InstaUserSerializer(users, many=True)
        return JsonResponse({'users': serializer.data}, status=200)

    def put(self, request):
        user = get_object_or_None(InstaUser, id=request.data['id'])
        if user:
            serializer = InstaUserEditSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'user': serializer.data}, status=201)
            else:
                return JsonResponse({'message': serializer.errors}, status=400)
        else:
            return JsonResponse({'message': 'user not found'}, status=404)

    def delete(self, request):
        user = get_object_or_None(InstaUser, id=request.data['id'])
        if user:
            user.delete()
            return JsonResponse({'message': 'user deleted'}, status=200)
        else:
            return JsonResponse({'message': 'user not found'}, status=404)


