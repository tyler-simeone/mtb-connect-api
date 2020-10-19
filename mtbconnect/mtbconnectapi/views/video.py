from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Video

class VideoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Video
        url = serializers.HyperlinkedIdentityField(
            view_name='videos',
            lookup_field='id'
        )
        fields = ('id', 'video_url', 'trail_id')

class Videos(ViewSet):


    def retrieve(self, request, pk=None):

        try:
            video = Video.objects.get(pk=pk)

            serializer = VideoSerializer(
                video, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        
        videos = Video.objects.all()

        serializer = VideoSerializer(
            videos, many=True, context={'request': request})

        return Response(serializer.data)
