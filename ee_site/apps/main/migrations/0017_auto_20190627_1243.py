# Generated by Django 2.2.2 on 2019-06-27 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('main', '0016_auto_20190624_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='join_us_background',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='join_us_body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='join_us_body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='join_us_body_pl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='join_us_headline',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='join_us_headline_en',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='join_us_headline_pl',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
