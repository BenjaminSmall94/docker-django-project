from rest_framework import serializers
from .models import Stuff


class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'explanation', 'time_stamp_creation')
        model = Stuff
