# Generated by Django 5.1.7 on 2025-03-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='operation',
            field=models.CharField(choices=[('add', 'add'), ('sub', 'sub'), ('mul', 'mul'), ('div', 'div')], max_length=5),
        ),
    ]
