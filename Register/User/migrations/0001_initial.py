# Generated by Django 3.2.7 on 2022-01-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('mobile_no', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('Select_User', models.CharField(max_length=255)),
            ],
        ),
    ]