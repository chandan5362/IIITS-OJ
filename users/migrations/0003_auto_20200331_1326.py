# Generated by Django 3.0.4 on 2020-03-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200331_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ac_solution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='ce_solution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='hrating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='star',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='tle_solution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='wa_solution',
            field=models.IntegerField(default=0),
        ),
    ]
