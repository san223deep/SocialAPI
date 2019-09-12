# Generated by Django 2.2.4 on 2019-09-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20190912_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='adm', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]