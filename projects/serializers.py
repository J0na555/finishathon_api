from rest_framework import serializers
from .models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'github_link', 'video_demo', 'user', 'hackathon', 'created_at']
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        # If a request user is available in context, assign it as the owner
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            validated_data['user'] = request.user
        return super().create(validated_data)