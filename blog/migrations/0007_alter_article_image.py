# Generated by Django 4.1.3 on 2022-12-05 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='articles', verbose_name='Imagen'),
        ),
    ]
