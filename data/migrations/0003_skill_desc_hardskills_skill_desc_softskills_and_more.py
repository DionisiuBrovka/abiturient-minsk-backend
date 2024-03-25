# Generated by Django 4.2.7 on 2024-03-25 09:37

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_skill_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='desc_hardskills',
            field=models.TextField(blank=True, null=True, verbose_name='Вы получите навыки по:'),
        ),
        migrations.AddField(
            model_name='skill',
            name='desc_softskills',
            field=models.TextField(blank=True, null=True, verbose_name='Мы поможеи развить следующие профессиональные умения'),
        ),
        migrations.AddField(
            model_name='skill',
            name='desc_work',
            field=models.TextField(blank=True, null=True, verbose_name='Кем вы сможете работать'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Общее описание'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=data.models.skillWrapper, verbose_name='Фото карточки'),
        ),
    ]
