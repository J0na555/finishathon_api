from django.contrib import admin
from .models import Projects


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'hackathon', 'created_at')
	list_filter = ('hackathon', 'created_at')
	search_fields = ('title', 'description', 'user__username')
