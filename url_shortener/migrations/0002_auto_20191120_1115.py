# Generated by Django 2.2.7 on 2019-11-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='lifetime',
            field=models.IntegerField(default=90),
        ),
    ]
