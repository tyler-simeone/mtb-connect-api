from django.http import HttpResponseServerError
from django.contrib.auth.models import User as AuthUser
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

    def put(self, request, pk=None):
        """Handle PUT requests for an individual user
        Returns:
            Response -- Empty body with 204 status code
        """
        user = User.objects.get(user_id=pk)
        auth_user = AuthUser.objects.get(pk=pk)

        auth_user.first_name = request.data["first_name"]
        auth_user.last_name = request.data["last_name"]
        user.avatar_img = request.data["avatar_img"]
        auth_user.username = request.data["username"]
        auth_user.email = request.data["email"]
        

        user.save()
        auth_user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
   
    def list(self, request):

        try:
            users_list = User.objects.all()

            serializer = UserSerializer(
                users_list, many=True, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)