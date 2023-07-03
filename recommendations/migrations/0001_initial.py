# Generated by Django 4.1.4 on 2023-06-30 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Logins', '0001_initial'),
        ('Workouts', '0001_initial'),
        ('Meals', '0003_remove_recipe_name_recipe_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Meals.mealplan')),
                ('recommended_workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Workouts.workout')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Logins.userprofile')),
            ],
        ),
    ]