# Generated by Django 4.1.4 on 2023-07-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workouts', '0005_exercise_workout_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='workout_picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]