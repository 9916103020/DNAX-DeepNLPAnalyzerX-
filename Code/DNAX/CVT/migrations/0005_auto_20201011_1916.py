# Generated by Django 3.1.2 on 2020-10-11 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CVT', '0004_auto_20201010_1829'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='files',
            unique_together={('company', 'version')},
        ),
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
    ]