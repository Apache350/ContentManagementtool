# Generated by Django 4.1.3 on 2023-07-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='Text',
            field=models.CharField(default='NA', max_length=20000),
        ),
    ]
