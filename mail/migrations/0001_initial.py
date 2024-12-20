# Generated by Django 5.1.3 on 2024-11-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=256, null=True)),
                ('body', models.TextField(null=True, verbose_name='body')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=254, null=True, verbose_name='last_name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('mail_body_field', models.TextField(default='no message', null=True, verbose_name='mail_body_field')),
            ],
        ),
    ]
