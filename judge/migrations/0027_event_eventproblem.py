# Generated by Django 3.0.4 on 2020-07-21 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('judge', '0026_problem_difficultylevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('statement', froala_editor.fields.FroalaField(blank='true')),
                ('constraint', froala_editor.fields.FroalaField(blank='true')),
                ('input_format', models.TextField()),
                ('output_format', models.TextField()),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('explaination', models.TextField()),
                ('time_limit', models.IntegerField(default=1)),
                ('input_file', models.FileField(upload_to='inputs/')),
                ('output_file', models.FileField(upload_to='outputs/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=400)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('problems', models.ManyToManyField(to='judge.EventProblem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]