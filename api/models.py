from django.db import models
from django.contrib.gis.db import models as geomodels
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Reserves(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    geom = geomodels.MultiPolygonField()
    pictures = models.ManyToManyField('ReviewsPictures',related_name='picture_url')
    class Meta:
        verbose_name_plural = 'Заповедники'
        verbose_name = 'Заповедник'

    def __str__(self):
        return self.name


class Routes(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    COMPLEXITY_CHOICES = (

        (1, '1'),

        (2, '2'),

        (3, '3'),

        (4, '4'),

        (5, '5'),

    )
    сomplexity = models.IntegerField(choices=COMPLEXITY_CHOICES, default='1', verbose_name='Сложность')
    geom = geomodels.MultiLineStringField()
    reserve = models.ForeignKey(Reserves, blank=True, null=True, on_delete=models.CASCADE,
                             verbose_name='Заповедник',
                             related_name='Route')
    class Meta:
        verbose_name_plural = 'Маршруты'
        verbose_name = 'Маршрут'

    def __str__(self):
        return self.name


class Sights(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=512, blank=True, null=True)
    reserve = models.ForeignKey(Reserves, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Заповедник',
                                 related_name='SightReserve')
    geom = geomodels.PointField()
    class Meta:
        verbose_name_plural = 'Достопримечательности'
        verbose_name = 'Достопримечательность'

    def __str__(self):
        return self.name


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    known_routes = models.ManyToManyField('Routes',blank=True)
    is_guide = models.BooleanField(default=False)
    achievements = models.ManyToManyField('Achievements',blank=True)
    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
    def __str__(self):
        return self.user.username

class ReserveReview(models.Model):
    text = models.TextField(blank=True, null=True)
    RATING_CHOICES = (

        (1, '1'),

        (2, '2'),

        (3, '3'),

        (4, '4'),

        (5, '5'),

    )
    pictures = models.ManyToManyField('ReviewsPictures',blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default='5', verbose_name='Рейтинг')
                            
    reserve = models.ForeignKey(Reserves, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Заповедник',
                                 related_name='ReserveReview')
    user = models.ForeignKey(userProfile, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Пользователь',
                                 related_name='ReserveReviewUser')

    class Meta:
        verbose_name_plural = 'Отзывы о заповеднинках'
        verbose_name = 'Отзыв о заповеднинке'



class RouteReview(models.Model):
    text = models.TextField(blank=True, null=True)
    RATING_CHOICES = (

        (1, '1'),

        (2, '2'),

        (3, '3'),

        (4, '4'),

        (5, '5'),

    )
    pictures = models.ManyToManyField('ReviewsPictures', blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default='5', verbose_name='Рейтинг')          
    route = models.ForeignKey(Reserves, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Маршрут',
                                 related_name='RouteReview')
    user = models.ForeignKey(userProfile, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Пользователь',
                                 related_name='RouteReviewUser')
    class Meta:
        verbose_name_plural = 'Отзывы о маршрутах'
        verbose_name = 'Отзыв о маршруте'

class ReviewsPictures(models.Model):
    picture = models.ImageField(upload_to='picture')
    picture_thumbnail = ImageSpecField(source='picture',
                                  processors=[ResizeToFill(300, 300)],
                                  format='JPEG',
                                  options={'quality': 60})
    class Meta:
        verbose_name_plural = 'Картинки'
        verbose_name = 'Картинка'
    def __str__(self):
        return self.picture.name


class Achievements(models.Model):
        name = models.CharField(max_length=256, blank=True, null=True)
        img = models.ImageField(upload_to='picture')
        goal = JSONField(blank=True, null=True,)
        class Meta:
            verbose_name_plural = 'Доcтижения'
            verbose_name = 'Доcтижение'

class Trips(models.Model):
        name = models.CharField(max_length=256, blank=True, null=True)
        text = models.TextField(blank=True, null=True)
        route = models.ForeignKey(Routes, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Маршрут',
                                 related_name='TripRoute')
        reserve = models.ForeignKey(Reserves, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Заповедник',
                                 related_name='TripReserve')
        guide = models.ForeignKey(userProfile, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Гид',
                                 related_name='GuideAccount')
        start_date=models.DateTimeField()
        end_date=models.DateTimeField()
        group = models.ManyToManyField('userProfile', blank=True)
        class Meta:
            verbose_name_plural = 'Походы'
            verbose_name = 'Поход'
        def save(self):
            self.reserve = self.route.reserve
            super(Trips, self).save()
        def __str__(self):
            return self.name


class GeoCash(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    descr = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=512, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    reserve = models.ForeignKey(Reserves, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Заповедник',
                                 related_name='GeoCashReserve')
    geom = geomodels.PointField()
    class Meta:
        verbose_name_plural = 'Достопримечательности'
        verbose_name = 'Достопримечательность'

    def __str__(self):
        return self.name
