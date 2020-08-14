from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Friend

class FriendSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Friend
        url = serializers.HyperlinkedIdentityField(
            view_name='friend',
            lookup_field='id'
        )
        fields = ('id', 'requestPending', 'requestAccepted', 'receiver_id', 'sender_id')

class Friends(ViewSet):

    # def create(self, request):
    
    #     new_trail = Trail()
    #     new_trail.trail_name = request.data["trail_name"]
    #     new_trail.trail_img = request.data["trail_img"]
    #     new_trail.description = request.data["description"]
    #     new_trail.address = request.data["address"]
    #     new_trail.zipcode = request.data["zipcode"]
    #     new_trail.creator_id = request.data["creator_id"]

    #     new_trail.save()

    #     serializer = TrailSerializer(
    #         new_trail, context={'request': request})

    #     return Response(serializer.data)

    # REVIEW: So I learned something new here... Need a retrieve method
    # in order to run a PUT request (404 on the PUT w/o the retrieve method)
    def retrieve(self, request, pk=None):

        try:
            friend = Friend.objects.get(pk=pk)

            serializer = FriendSerializer(
                friend, context={'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def put(self, request, pk=None):
        """Handle PUT requests for an individual trail
        Returns:
            Response -- Empty body with 204 status code
        """
        friend = Friend.objects.get(pk=pk)
        friend.sender_id = request.data["senderId"]
        friend.receiver_id = request.data["receiverId"]
        friend.requestPending = request.data["isRequestPending"]
        friend.requestAccepted = request.data["isAccepted"]
        friend.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

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

    def list(self, request):
        
        friends = Friend.objects.all()

        request_receiver = self.request.query_params.get('receiverId')
        request_sender = self.request.query_params.get('senderId')
        request_status = self.request.query_params.get('isAccepted')

        # Returns friends that sent user req, and user accepted
        if request_receiver and request_status:
            friends = Friend.objects.filter(receiver_id=request_receiver, requestAccepted=request_status)

        # Returns friends that user sent req to, and friends accepted
        if request_sender and request_status:
            friends = Friend.objects.filter(sender_id=request_sender, requestAccepted=request_status)

        elif request_receiver is not None:
            friends = Friend.objects.filter(receiver_id=request_receiver)

        serializer = FriendSerializer(
            friends, many=True, context={'request': request})

        return Response(serializer.data)
