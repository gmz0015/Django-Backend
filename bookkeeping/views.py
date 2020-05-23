from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from bookkeeping.models import Welcome
from bookkeeping.serializears import WelcomeSerializer


class WelcomeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Welcome.objects.all()
    serializer_class = WelcomeSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Welcome.objects.all()
    serializer_class = WelcomeSerializer

    def list(self, request, *args, **kwargs):
        if self.request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = self.request.META.get('HTTP_X_FORWARDED_FOR')
        else:
            ip = self.request.META.get('REMOTE_ADDR')

        print("ip: {}".format(ip))
        # welcome = Welcome(fromIP=ip)
        # welcome.save()
        serializer = WelcomeSerializer(data={'fromIP':ip})
        if serializer.is_valid():
            serializer.save()
            print("serializer: {}".format(serializer.data))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
