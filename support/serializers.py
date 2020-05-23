from support.models import Token
from rest_framework import serializers


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    # token = serializers.HyperlinkedIdentityField('token', lookup_field='token')

    class Meta:
        model = Token
        fields = ['time', 'token']