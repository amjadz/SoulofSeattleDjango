# Generated by Django 3.0 on 2020-02-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulofseattlepages', '0012_auto_20200214_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_image_upload',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_biography',
            field=models.TextField(),
        ),
    ]
