from django.contrib import admin
from django.urls import path, include
from users.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hackathons/', include('hackathons.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/users/', include('users.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('dj-rest-auth/social/', include('dj_rest_auth.social_urls')),
    path('accounts/', include('allauth.urls')),
    # explicit Google social-login endpoint (used by Postman / frontend)
    path('dj-rest-auth/registration/google/', GoogleLogin.as_view(), name='google_login'),
]
