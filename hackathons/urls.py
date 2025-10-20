from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import HackathonViewSet, ActiveHackathon, PastHackathons

router = DefaultRouter()
router.register(r'hackathons', HackathonViewSet)

# having router in this urls helps in making the urls neat like
# in other words it helps put the crud operations in one line
# automatically generates urls

#           /	        GET	        list()	            hackathon-list
#           / 	        POST	    create()	        hackathon-list
#           /{pk}/	    GET	        retrieve()	        hackathon-detail
#           /{pk}/	    PUT	        update()	        hackathon-detail
#           /{pk}/	    PATCH	    partial_update()	hackathon-detail
#           /{pk}/	    DELETE	    destroy()	        hackathon-detail

urlpatterns = [
    path('', include(router.urls)),
    path('active/', ActiveHackathon.as_view(), name='active-hackathon'),
    path('past/', PastHackathons.as_view(), name='past-hackathons'),
]

