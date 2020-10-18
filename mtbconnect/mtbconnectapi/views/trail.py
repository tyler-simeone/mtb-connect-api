from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Trail, Video

class TrailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Trail
        url = serializers.HyperlinkedIdentityField(
            view_name='trail',
            lookup_field='id'
        )
        fields = ('id', 'trail_name', 'trail_img', 'description', 'address',
                  'zipcode', 'creator_id')

class Trails(ViewSet):

    def create(self, request):
    
        new_trail = Trail()
        new_trail.trail_name = request.data["trail_name"]
        new_trail.trail_img = request.data["trail_img"]
        new_trail.description = request.data["description"]
        new_trail.address = request.data["address"]
        new_trail.zipcode = request.data["zipcode"]
        new_trail.creator_id = request.data["creator_id"]

        new_trail.save()

        serializer = TrailSerializer(
            new_trail, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            trail = Trail.objects.get(pk=pk)

            videos = Video.objects.get(pk=trail.video_id)

            trail.videos = videos

            serializer = TrailSerializer(
                trail, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def put(self, request, pk=None):
        """Handle PUT requests for an individual trail
        Returns:
            Response -- Empty body with 204 status code
        """
        trail = Trail.objects.get(pk=pk)
        trail.trail_name = request.data["trail_name"]
        trail.trail_img = request.data["trail_img"]
        trail.description = request.data["description"]
        trail.address = request.data["address"]
        trail.zipcode = request.data["zipcode"]
        trail.creator_id = request.data["creator_id"]
        trail.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single trail
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            trail = Trail.objects.get(pk=pk)
            trail.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Trail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        
        trails = Trail.objects.all()

        zipcode = self.request.query_params.get('zipcode')

        if zipcode is not None:
            trails = Trail.objects.filter(zipcode = zipcode)

        serializer = TrailSerializer(
            trails, many=True, context={'request': request})

        return Response(serializer.data)
