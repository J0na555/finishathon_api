from rest_framework import serializers
from .models import  Hackathon

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ['id', 'title', 'theme', 'created_at', 'start_time', 'end_time', 'is_active']
        read_only_fields = ('id' ,'created_at', 'is_active')

