from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Users
        fields = ['email', 'fam', 'name', 'otc', 'phone',]


class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height',]


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring',]


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['data', 'title',]


class PerevalAddedSerializer(WritableNestedModelSerializer):
    user_id = UsersSerializer()
    coords_id = CoordsSerializer()
    level_id = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user_id', 'coords_id', 'level_id', 'images']
