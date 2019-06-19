# Generated by Django 2.2.1 on 2019-05-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190528_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='r_and_d_center_body_en',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='r_and_d_center_body_pl',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='r_and_d_center_headline_en',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='r_and_d_center_headline_pl',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='specializations_headline_en',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='specializations_headline_pl',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
