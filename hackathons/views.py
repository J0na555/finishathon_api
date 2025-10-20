from hackathons.models import Hackathon
from .serializers import HackathonSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from django.utils import timezone


class HackathonViewSet(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [permissions.IsAdminUser]


class ActiveHackathon(generics.ListAPIView):
    serializer_class = HackathonSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Returns currently active hackathons.

        A hackathon is active if:
        - is_active == True
        - start_time <= now <= end_time
        """
        current_time = timezone.now()
        return Hackathon.objects.filter(
            is_active=True,
            start_time__lte=current_time,
            end_time__gte=current_time,
        )


class PastHackathons(generics.ListAPIView):
    serializer_class = HackathonSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        current_time = timezone.now()
        return Hackathon.objects.filter(end_time__lt=current_time).order_by('-end_time')
    
            