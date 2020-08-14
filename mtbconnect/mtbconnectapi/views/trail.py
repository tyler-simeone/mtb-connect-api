from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Trail

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

            serializer = TrailSerializer(
                trail, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)
