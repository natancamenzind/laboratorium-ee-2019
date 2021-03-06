# Generated by Django 2.2.1 on 2019-05-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190528_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='RodoPassAdvert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_pl', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=256)),
                ('description_pl', models.CharField(max_length=256, null=True)),
                ('description_en', models.CharField(max_length=256, null=True)),
                ('url', models.URLField()),
                ('button_text', models.CharField(max_length=50)),
                ('button_text_pl', models.CharField(max_length=50, null=True)),
                ('button_text_en', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
