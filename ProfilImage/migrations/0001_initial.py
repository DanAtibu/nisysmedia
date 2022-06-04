# Generated by Django 4.0.3 on 2022-03-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Profiles/')),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UserId', models.IntegerField(null=True)),
            ],
        ),
    ]
