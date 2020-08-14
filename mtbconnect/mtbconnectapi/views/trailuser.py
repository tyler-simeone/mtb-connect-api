from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import TrailUser

class TrailUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TrailUser
        url = serializers.HyperlinkedIdentityField(
            view_name='trailuser',
            lookup_field='id'
        )
        fields = ('id', 'trail_id', 'user_id')

class TrailUsers(ViewSet):

    def create(self, request):
    
        new_trail_user = TrailUser()
        new_trail_user.trail_id = request.data["trail_id"]
        new_trail_user.user_id = request.data["user_id"]

        new_trail_user.save()

        serializer = TrailUserSerializer(
            new_trail_user, context={'request': request})

        return Response(serializer.data)

    # def destroy(self, request, pk=None):
    #     """Handle DELETE requests for a single trail
    #     Returns:
    #         Response -- 200, 404, or 500 status code
    #     """
    #     try:
    #         trail = Trail.objects.get(pk=pk)
    #         trail.delete()

    #         return Response({}, status=status.HTTP_204_NO_CONTENT)

    #     except Trail.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    #     except Exception as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def list(self, request):
        
    #     trails = Trail.objects.all()

    #     zipcode = self.request.query_params.get('zipcode')

    #     if zipcode is not None:
    #         trails = Trail.objects.filter(zipcode = zipcode)

    #     serializer = TrailUserSerializer(
    #         trails, many=True, context={'request': request})

    #     return Response(serializer.data)
