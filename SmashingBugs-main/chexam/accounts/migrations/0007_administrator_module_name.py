# Generated by Django 4.0.4 on 2022-05-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_teacher_module_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='module_name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
