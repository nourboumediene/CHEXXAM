# Generated by Django 4.0.4 on 2022-05-27 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_alter_result_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='solution',
            field=models.FileField(default=None, upload_to='Solutions'),
        ),
        migrations.AddField(
            model_name='problem',
            name='scan',
            field=models.FileField(default=None, upload_to='test'),
        ),
        migrations.AlterField(
            model_name='result',
            name='scan',
            field=models.FileField(default=None, upload_to='test'),
        ),
    ]
