# Generated by Django 4.1.7 on 2023-03-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headings', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
