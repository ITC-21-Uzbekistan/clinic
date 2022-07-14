from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.direction.models import Direction
from apps.direction.serializers.serializers import DirectionSerializers


class ListCreateDirectionAPIView(ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RetrieveUpdateDestroyDirectionAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

