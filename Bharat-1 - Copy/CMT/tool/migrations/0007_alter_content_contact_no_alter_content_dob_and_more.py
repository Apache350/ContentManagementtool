# Generated by Django 4.1.3 on 2023-07-20 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0006_alter_content_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='Contact_no',
            field=models.PositiveIntegerField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='content',
            name='DOB',
            field=models.DateField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='content',
            name='Email',
            field=models.EmailField(blank=True, default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='content',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans'), ('Prefer not to say', 'Prefer not to say')], default=' ', max_length=30),
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=200),
        ),
    ]
