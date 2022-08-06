from rest_framework.routers import DefaultRouter

from itineraries import views

router = DefaultRouter()
router.register(r"itineraries", views.ItineraryView, basename="Itinerary")


urlpatterns = router.urls
