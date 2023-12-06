from django.db import models
import os
from uuid import uuid4

# Create your models here.
class Establishment(models.Model):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join('est/', filename)

    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название учреждения образования")
    short_title = models.CharField(max_length=35, null=False, blank=False, verbose_name="Сокращенное название")

    desc = models.TextField(null=True, blank=True, verbose_name="Описание")
    adress = models.CharField(max_length=255, null=False, blank=False, verbose_name="Адрес")

    tel = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер телефона")
    mail = models.CharField(max_length=255, null=True, blank=True, verbose_name="Почтовые реквизиты")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почта")
    wsite = models.URLField(null=True,blank=True,verbose_name="Веб сайт")
    wtel = models.URLField(null=True,blank=True,verbose_name="Телеграм")
    wvk = models.URLField(null=True,blank=True,verbose_name="Вк")
    winsta = models.URLField(null=True,blank=True,verbose_name="Инстаграм")
    wother = models.URLField(null=True,blank=True,verbose_name="Прочее")

    specialty = models.ManyToManyField('Specialty', null=True, blank=True, verbose_name="Специальности")

    icon = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Логотип")
    prev = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Превью")
    promo_medio = models.FileField(upload_to=wrapper, null=True, blank=True, verbose_name="Промо ролик")

    coords = models.CharField(max_length=255, null=True, blank=True, verbose_name="Координаты на карте") 

    def __str__(self) -> str:
        return self.short_title

    class Meta:
        verbose_name = "Образовательное учреждение"
        verbose_name_plural = "Образовательные учреждения"


class Event(models.Model):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join('event/', filename)

    e_date = models.DateTimeField(null=False, blank=False, verbose_name="Дата мероприятия")
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название мероприятия")
    desc = models.TextField(null=False,blank=False, verbose_name="Описание")
    prev = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Превью")

    org = models.ForeignKey('Establishment', models.CASCADE, related_name="events", null=True, blank=True, verbose_name="Организатор" )
    e_url = models.URLField(null=True, blank=True, verbose_name="Ссылка на страницу мероприятия")

    def __str__(self) -> str:
        return str(self.e_date) + " " + self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Gallery(models.Model):
    
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join('gallery/', filename)

    photo = models.ImageField(upload_to=wrapper, null=False, blank=False, verbose_name="Превью")
    desc = models.TextField(null=False, blank=False, verbose_name="Описание")
    est = models.ForeignKey('Establishment', models.CASCADE, related_name="gallery", null=True, blank=True, verbose_name="УО")

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"


class SpecialtyGroup(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название группы специальностей")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Группа специальностей"
        verbose_name_plural = "Группы специальностей"


class Specialty(models.Model):

    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join('spec/', filename)

    COISES = [
        ("S","ССО"),
        ("P","ПТО"),
    ]

    SOISES = [
        ("9","На основе общего базового образования (после 9 кл.)"),
        ("11","На основе общего среднего образования (после 11 кл.)"),
        ("PTO","На основе ПТО"),
    ]

    c_type = models.CharField(max_length=1, choices=COISES, null=False, blank=False, verbose_name="Тип")
    s_type = models.CharField(max_length=3, choices=SOISES, null=False, blank=False, verbose_name="На базе ...")
    group = models.ForeignKey('SpecialtyGroup', models.CASCADE, null=False , blank=False, verbose_name="Группа специальностей")
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name="Код")
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название специальности")
    skill = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название квалификации")
    prev = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Превью")
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")

    icon = models.CharField(max_length=255, null=True, blank=True, verbose_name="ИД иконки флаттер")

    def __str__(self) -> str:
        return self.code + " // " + self.title

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class FAQ(models.Model):

    q = models.TextField(null=False, blank=False, verbose_name="Вопрос")
    a = models.TextField(null=False, blank=False, verbose_name="Ответ")

    def __str__(self) -> str:
        return str(self.id) + " // " + self.q

    class Meta:
        verbose_name = "Вопрос - Ответ"
        verbose_name_plural = "Вопрос - Ответ"
