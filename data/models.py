from django.db import models
import os
from uuid import uuid4

def wrapper(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return filename

def establishmentWrapper(instance, filename):
    return os.path.join('establishments/', wrapper(instance, filename))

def eventWrapper(instance, filename):
    return os.path.join('events/', wrapper(instance, filename))

def galleryWrapper(instance, filename):
    return os.path.join('gallerys/', wrapper(instance, filename))

def specialtyWrapper(instance, filename):
    return os.path.join('specialtys/', wrapper(instance, filename))

def skillWrapper(instance, filename):
    return os.path.join('skills/', wrapper(instance, filename))


# УО 
class Establishment(models.Model):

    wrapper = establishmentWrapper

    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название учреждения образования")
    short_title = models.CharField(max_length=35, null=False, blank=False, verbose_name="Сокращенное название")

    desc = models.TextField(null=True, blank=True, verbose_name="Описание")
    adress = models.CharField(max_length=255, null=False, blank=False, verbose_name="Адрес")

    tel = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер телефона")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почта")
    wsite = models.URLField(null=True,blank=True,verbose_name="Веб сайт")
    wtel = models.URLField(null=True,blank=True,verbose_name="Телеграм")
    wvk = models.URLField(null=True,blank=True,verbose_name="Вк")
    winsta = models.URLField(null=True,blank=True,verbose_name="Инстаграм")
    wface = models.URLField(null=True,blank=True,verbose_name="Фейсбук")
    wtwit = models.URLField(null=True,blank=True,verbose_name="Твиттер")
    wtic = models.URLField(null=True,blank=True,verbose_name="Тик-ток")
    wother = models.URLField(null=True,blank=True,verbose_name="Прочее")

    icon = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Логотип")
    prev = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Превью")
    promo_medio = models.FileField(upload_to=wrapper, null=True, blank=True, verbose_name="Промо ролик")

    coords = models.CharField(max_length=255, null=True, blank=True, verbose_name="Координаты на карте") 

    def __str__(self) -> str:
        return self.short_title

    class Meta:
        ordering = ['-title']
        verbose_name = "Образовательное учреждение"
        verbose_name_plural = "Образовательные учреждения"


# Мероприятия
class Event(models.Model):

    wrapper = eventWrapper

    e_date = models.DateTimeField(null=False, blank=False, verbose_name="Дата мероприятия")
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название мероприятия")
    desc = models.TextField(null=False, blank=False, verbose_name="Описание")
    prev = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Превью")

    org = models.ForeignKey('Establishment', models.CASCADE, related_name="events", null=True, blank=True, verbose_name="Организатор" )
    e_url = models.URLField(null=True, blank=True, verbose_name="Ссылка на страницу мероприятия")

    def __str__(self) -> str:
        return str(self.e_date) + " " + self.title

    class Meta:
        ordering = ['-e_date']
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


# Фоточки УО
class Gallery(models.Model):
    
    wrapper = galleryWrapper

    est = models.ForeignKey('Establishment', models.CASCADE, related_name="gallery", null=False, blank=False, verbose_name="УО")
    photo = models.ImageField(upload_to=wrapper, null=False, blank=False, verbose_name="Превью")
    desc = models.TextField(null=False, blank=False, verbose_name="Описание")

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"


# Группы специальностей
class SpecialtyGroup(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название группы специальностей")

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name = "Группа специальностей"
        verbose_name_plural = "Группы специальностей"


# Специальности
class Specialty(models.Model):

    wrapper = specialtyWrapper

    COISES = [
        ("ССО","ССО"),
        ("ПТО","ПТО"),
    ]

    code = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name="Код")
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название специальности")
    c_type = models.CharField(max_length=3, choices=COISES, null=False, blank=False, verbose_name="Тип")
    
    group = models.ForeignKey('SpecialtyGroup', models.CASCADE, null=True , blank=True, verbose_name="Группа специальностей")
    
    prev = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Превью")
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")

    icon = models.CharField(max_length=255, null=True, blank=True, verbose_name="ИД иконки флаттер")

    def __str__(self) -> str:
        return f"{self.code} // {self.title} // {self.c_type}"

    class Meta:
        ordering = ['title']
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


# Квалификации
class Skill(models.Model):

    wrapper = skillWrapper

    code = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name="Код")
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название квалификации")
    searchtag = models.TextField(null=True, blank=True, verbose_name="Теги для поиска")

    specialty = models.ForeignKey('Specialty', models.CASCADE, related_name="skills", null=False , blank=False, verbose_name="Специальность")
    
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to=wrapper, null=True, blank=True, verbose_name="Описание фото")

    def __str__(self) -> str:
        return f"{self.code} // {self.title} // "

    class Meta:
        ordering = ['code']
        verbose_name = "Квалификация"
        verbose_name_plural = "Квалификации"


# Смежная таблица
class SkillForEstablishment(models.Model):

    SOISES = [
        ("9","На основе общего базового образования (после 9 кл.)"),
        ("11","На основе общего среднего образования (после 11 кл.)"),
        ("ПТО","На основе ПТО"),
    ]

    est = models.ForeignKey('Establishment', models.CASCADE, related_name="skills", null=False, blank=False, verbose_name="УО")
    # skill = models.ForeignKey('Skill', models.CASCADE, related_name="svod", null=False , blank=False, verbose_name="Квалификация")
    skill = models.ManyToManyField('skill', related_name="svod", null=False , blank=False, verbose_name="Квалификация")
    s_type = models.CharField(max_length=3, choices=SOISES, null=False, blank=False, verbose_name="На базе ...")

    b_count = models.IntegerField(null=True, blank=True, verbose_name="Количество набора на бюджет")
    b_long = models.CharField(max_length=255, null=True, blank=True, verbose_name="Продолжительность обучения на бюджете")
    b_avd = models.FloatField(null=True, blank=True, verbose_name="Средний балл бюджет")

    p_count = models.IntegerField(null=True, blank=True, verbose_name="Количество набора на платное")
    p_long = models.CharField(max_length=255, null=True, blank=True, verbose_name="Продолжительность обучения на платном")
    p_avd = models.FloatField(null=True, blank=True, verbose_name="Средний балл платное")

    rule = models.CharField(max_length=255, null=True, blank=True, verbose_name="Правила набора")
    
    is_opfr = models.BooleanField(default=False, verbose_name="Введется ли набор обучающихся с ОПФР")
    opfr_qnic = models.CharField(max_length=255, null=True, blank=True, verbose_name="Особенности ОПФР")


    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name = "Сводная таблица"
        verbose_name_plural = "Сводная таблица"


# Вопрос ответ
class FAQ(models.Model):

    q = models.TextField(null=False, blank=False, verbose_name="Вопрос")
    a = models.TextField(null=False, blank=False, verbose_name="Ответ")

    def __str__(self) -> str:
        return str(self.id) + " // " + self.q

    class Meta:
        ordering = ['q']
        verbose_name = "Вопрос - Ответ"
        verbose_name_plural = "Вопрос - Ответ"
