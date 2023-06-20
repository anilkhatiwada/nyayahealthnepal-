from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Practitioner
from .serializer import PractitionerSerializer


class PractitionerView(APIView):
    """
    API view for the Practitioner resource.
    """

    serializer_class = PractitionerSerializer

    def get(self, request, pk=None):
        """
        Retrieve a Practitioner resource.
        """
        if pk is None:
            practitioners = Practitioner.objects.all()
            serializer = self.serializer_class(practitioners, many=True)
            return Response(serializer.data)
        else:
            practitioner = Practitioner.objects.get(pk=pk)
            serializer = self.serializer_class(practitioner)
            return Response(serializer.data)

    def post(self, request):
        """
        Create a new Practitioner resource.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            practitioner = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update an existing Practitioner resource.
        """
        practitioner = Practitioner.objects.get(pk=pk)
        serializer = self.serializer_class(practitioner, data=request.data)
        if serializer.is_valid():
            practitioner = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a Practitioner resource.
        """
        try:
            practitioner = Practitioner.objects.get(pk=pk)
            practitioner.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Practitioner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

