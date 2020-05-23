from rest_framework import serializers

from bookkeeping.models import STYLE_CHOICES, Welcome


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = ['id', 'time', 'fromIP', 'word']