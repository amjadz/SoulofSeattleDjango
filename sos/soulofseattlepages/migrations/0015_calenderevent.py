# Generated by Django 3.0 on 2020-03-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulofseattlepages', '0014_auto_20200214_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalenderEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('event_description', models.TextField()),
            ],
        ),
    ]
