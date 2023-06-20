from rest_framework import serializers
from .models import Practitioner


class PractitionerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Practitioner resource.
    """

    class Meta:
        model = Practitioner
        fields = ('id', 'identifier', 'name', 'telecom', 'address', 'gender', 'birthDate', 'photo', 'roles', 'specialty')

