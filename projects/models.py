from django.db import models
from users.models import CustomUser
from hackathons.models import Hackathon

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    github_link = models.CharField(max_length=200)
    video_demo = models.FileField(upload_to="videos/")
    # A user can submit multiple projects and a hackathon can have many
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
