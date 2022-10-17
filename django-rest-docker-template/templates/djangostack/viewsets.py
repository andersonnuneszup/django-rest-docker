from rest_framework import status, viewsets
from rest_framework.response import Response

class AboutViewSet(viewsets.ViewSet):
    def about(self, request):
        return Response({'message': 'Django Rest Framework STACK'}, status.HTTP_200_OK)