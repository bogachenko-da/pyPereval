from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Users
        fields = ['email', 'fam', 'name', 'otc', 'phone',]

    def save(self, **kwargs):
        self.is_valid()
        user = Users.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = Users.objects.create(
                email=self.validated_data.get('email'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
                phone=self.validated_data.get('phone'),

            )
            return new_user


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
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'level', 'images']
