from .models import Projects
from rest_framework import generics, permissions
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# /api/projects/ → list (anyone) and create (authenticated)
class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Assign authenticated user as owner if not already provided
        serializer.save(user=self.request.user)


# /api/projects/user/ → list projects for the authenticated user
class UsersProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Projects.objects.filter(user=user).order_by('-created_at')
    



