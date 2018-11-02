# Generated by Django 2.1.1 on 2018-10-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181022_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connpass_Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn_results_returned', models.PositiveSmallIntegerField()),
                ('cn_results_available', models.PositiveSmallIntegerField()),
                ('cn_results_start', models.PositiveSmallIntegerField()),
                ('cn_event_id', models.PositiveIntegerField()),
                ('cn_title', models.CharField(max_length=150)),
                ('cn_catch', models.CharField(max_length=150)),
                ('cn_description', models.CharField(max_length=200)),
                ('cn_event_url', models.URLField()),
            ],
        ),
    ]