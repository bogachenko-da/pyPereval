from django.db import models


STATUS = [
    ('new', 'новый'),
    ('pending', 'на модерации'),
    ('accepted', 'принят'),
    ('rejected', 'не принят'),
]

LEVELS = [
    ('', 'не указано'),
    ('1A', '1a'),
    ('1B', '1б'),
    ('2А', '2а'),
    ('2В', '2б'),
    ('3А', '3а'),
    ('3В', '3б'),
    ]


class Users(models.Model):
    email = models.EmailField(verbose_name='Почта', max_length=255, unique=True)
    fam = models.CharField(verbose_name='Фамилия', max_length=32)
    name = models.CharField(verbose_name='Имя', max_length=32)
    otc = models.CharField(verbose_name='Отчество', max_length=32)
    phone = models.CharField(verbose_name='Телефон', max_length=15)


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта', max_length=9, blank=True)
    longitude = models.FloatField(verbose_name='Долгота', max_length=9, blank=True)
    height = models.FloatField(verbose_name='Высота', max_length=10, blank=True)


class Level(models.Model):
    winter = models.CharField(verbose_name='Зима', max_length=2, choices=LEVELS, default='')
    summer = models.CharField(verbose_name='Лето', max_length=2, choices=LEVELS, default='')
    autumn = models.CharField(verbose_name='Осень', max_length=2, choices=LEVELS, default='')
    spring = models.CharField(verbose_name='Весна', max_length=2, choices=LEVELS, default='')


class PerevalAdded(models.Model):
    beauty_title = models.CharField(verbose_name='Тип', max_length=10, default='пер. ')
    title = models.CharField(verbose_name='Название', max_length=64)
    other_titles = models.CharField(verbose_name='Другое название', max_length=64)
    connect = models.TextField(verbose_name='Что соединяет', max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=10, default='new')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    coords_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)


class Images(models.Model):
    data = models.ImageField(verbose_name='Фото', blank=True, null=True)
    title = models.CharField(verbose_name='Название', max_length=255, blank=True, null=True)
    pereval_id = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
