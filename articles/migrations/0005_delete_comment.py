# Generated by Django 2.2 on 2020-05-05 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
