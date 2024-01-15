from rest_framework import viewsets

from .models import Users, Coords, Level, Images, PerevalAdded
from .serializers import UsersSerializer, CoordsSerializer, LevelSerializer, ImagesSerializer, PerevalAddedSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevaAddedlViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
    filterset_fields = ('user__email', )
