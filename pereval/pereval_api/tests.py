from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PerevalAdded, Users, Coords, Level, Images
from .serializers import PerevalAddedSerializer


class PerevalAddedApiTestCase(APITestCase):
    """Класс тестов для тестирования функциональности веб-API"""
    def setUp(self):
        self.pereval_1 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="email1@mail.ru",
                fam="fam1",
                name="name1",
                otc="otc1",
                phone=89629117771
            ),

            beauty_title="beauty_title1",
            title="title1",
            other_titles="other_titles1",
            connect="connect1",

            coords=Coords.objects.create(
                latitude=9871.00,
                longitude=6541.00,
                height=1000
            ),

            level=Level.objects.create(
                winter="3B",
                summer="1A",
                autumn="2A",
                spring="2B"
            )
        )

        self.image_1_1 = Images.objects.create(
            title="pereval_1_image_1",
            data="https://url_pereval_1_image_1",
            pereval=self.pereval_1
        )

        self.image_1_2 = Images.objects.create(
            title="pereval_1_image_2",
            data="https://url_pereval_1_image_2",
            pereval=self.pereval_1
        )

        self.pereval_2 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="email2@mail.ru",
                fam="fam2",
                name="name2",
                otc="otc2",
                phone=89629117772
            ),

            beauty_title="beauty_title2",
            title="title2",
            other_titles="other_titles2",
            connect="connect2",

            coords=Coords.objects.create(
                latitude=9872.00,
                longitude=6542.00,
                height=2000
            ),

            level=Level.objects.create(
                winter="3A",
                summer="1B",
                autumn="2B",
                spring="2A"
            )
        )

        self.image_2_1 = Images.objects.create(
            title="pereval_2_image_1",
            data="https://url_pereval_2_image_1",
            pereval=self.pereval_2
        )

        self.image_2_2 = Images.objects.create(
            title="pereval_2_image_2",
            data="https://url_pereval_2_image_2",
            pereval=self.pereval_2
        )
