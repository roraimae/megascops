# Generated by Django 4.2.5 on 2023-11-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megascops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
