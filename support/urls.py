from django.urls import path, include

from rest_framework import routers

from support.views import TokenViewSet

router = routers.DefaultRouter()
router.register(r'token', TokenViewSet, basename='token')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]