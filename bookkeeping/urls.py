from django.urls import path, include

from rest_framework import routers

from bookkeeping.views import WelcomeViewSet, RegisterViewSet

router = routers.DefaultRouter()
router.register(r'home', WelcomeViewSet, basename='home')
router.register(r'register', RegisterViewSet, basename='register')


urlpatterns = [
    path('', include(router.urls))
]