# Generated by Django 4.1.3 on 2022-11-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Orden'),
        ),
    ]
