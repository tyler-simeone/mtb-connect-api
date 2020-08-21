from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )
        fields = ('id', 'user_id', 'user', 'avatar_img')

        depth = 1

class Users(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            user = User.objects.get(pk=pk)

            serializer = UserSerializer(
                user, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)
   
    def list(self, request):

        try:
            users_list = User.objects.all()

            serializer = UserSerializer(
                users_list, many=True, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)