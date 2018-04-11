# Generated by Django 2.0.2 on 2018-03-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_experiments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='targets',
            name='aeid',
        ),
        migrations.RemoveField(
            model_name='targets',
            name='intended_target_family',
        ),
        migrations.RemoveField(
            model_name='targets',
            name='intended_target_family_sub',
        ),
        migrations.RemoveField(
            model_name='targets',
            name='intended_target_type',
        ),
        migrations.RemoveField(
            model_name='targets',
            name='intended_target_type_sub',
        ),
        migrations.AlterField(
            model_name='targets',
            name='intended_target_description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='targets',
            name='technological_target_description',
            field=models.CharField(max_length=255),
        ),
    ]