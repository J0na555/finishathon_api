from django.db import models


class Hackathon(models.Model):
    title = models.CharField(max_length=50, unique=True)
    theme = models.CharField(max_length=50)
    created_at = models.DateField(auto_created=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


