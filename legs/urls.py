from rest_framework.routers import DefaultRouter

from legs import views

router = DefaultRouter()
router.register(r"legs", views.LegView, basename="Itinerary")


urlpatterns = router.urls
