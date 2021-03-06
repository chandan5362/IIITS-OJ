# Generated by Django 3.0.4 on 2020-03-13 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_solution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('solution', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='judge.Solution')),
                ('verdict', models.TextField()),
                ('time', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
