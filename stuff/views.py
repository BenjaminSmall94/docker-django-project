from .models import Stuff
from .serializers import StuffSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class StuffCreate(ListCreateAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer


class StuffList(ListAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer


class StuffDetail(RetrieveAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer


class StuffUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
