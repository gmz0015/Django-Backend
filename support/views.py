from django.middleware import csrf
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from support.serializers import TokenSerializer
from support.models import Token


# Create your views here.

class TokenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    @action(methods=['get'], detail=False)
    def token(self, request):
        queryset = Token(time=timezone.now(), token=csrf.get_token(request))
        serializer = TokenSerializer(queryset)
        return Response(serializer.data)

