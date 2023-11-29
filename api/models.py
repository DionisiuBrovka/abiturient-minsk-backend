from django.db import models

# Create your models here.
class Establishment(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название учреждения образования")
    short_title = models.CharField(max_length=35, null=False, blank=False, verbose_name="Сокращенное название")

    desc = models.TextField(null=True, blank=True, verbose_name="Описание")
    schedule = models.TextField(null=True, blank=True, verbose_name="График работы")
    contacts = models.ManyToManyField('Contact', verbose_name="Контакты")

    specialty = models.ManyToManyField('Specialty', verbose_name="Специальности")

    icon = models.ImageField(null=True, blank=True, verbose_name="Логотип")
    prev = models.ImageField(null=True, blank=True, verbose_name="Превью")
    promo_medio = models.FileField(null=True, blank=True, verbose_name="Промо ролик")

    coords = models.CharField(max_length=255, null=True, blank=True, verbose_name="Координаты на карте") 

    class Meta:
        verbose_name = "Образовательное учреждение"
        verbose_name_plural = "Образовательные учреждения"

class SpecialtyGroup(models.Model):

    COISES = [
        ("S","ССО"),
        ("P","ПТО"),
    ]

    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название группы специальностей")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="Код")
    g_type = models.CharField(max_length=1, choices=COISES, null=False, blank=False, verbose_name="Тип")
    icon = models.CharField(max_length=255, null=True, blank=True, verbose_name="Иконка")
    prev = models.ImageField(null=True, blank=True, verbose_name="Превью")
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Группа специальностей"
        verbose_name_plural = "Группы специальностей"

class Specialty(models.Model):

    group = models.ForeignKey('SpecialtyGroup', models.CASCADE, null=False , blank=False, verbose_name="Группа специальностей")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="Код")
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название специальности")
    skill = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название квалификации")
    prev = models.ImageField(null=True, blank=True, verbose_name="Превью")
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

class Contact(models.Model):

    CCOISES = [
        ("SIT","Сайт"),
        ("EMA","Электронная почта"),
        ("MAI","Древняя почта"),
        ("PHO","Номер"),
        ("TEL","Телеграм"),
        ("VIB","Вайбер"),
        ("VK","Вконтакте"),
        ("INS","Инстаграм"),
        ("FAC","Фейсбук"),
    ]

    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название контакта")
    c_type = models.CharField(max_length=3, choices=CCOISES, null=False, blank=False, verbose_name="Тип контакта" )
    email = models.EmailField(null=True, blank=True, verbose_name="Почта (если такой тип)")
    url = models.URLField(null=True, blank=True, verbose_name="УРЛ (если такой тип)")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон (если такой тип)")
    other = models.CharField(max_length=255, null=True, blank=True, verbose_name="Другое (если такой тип)")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"