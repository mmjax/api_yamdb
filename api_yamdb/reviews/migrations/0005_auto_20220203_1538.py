# Generated by Django 2.2.16 on 2022-02-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220202_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(blank=True),
        ),
    ]
