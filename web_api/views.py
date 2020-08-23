from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NowPlayingSerializer
from .models import NowPlaying

# Create your views here.
class NowPlayingView(viewsets.ModelViewSet):
    serializer_class = NowPlayingSerializer
    queryset = NowPlaying.objects.all()
