# Generated by Django 5.1.2 on 2024-10-28 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.TextField()),
                ('history', models.TextField()),
                ('content', models.TextField()),
                ('invite', models.TextField()),
            ],
        ),
    ]