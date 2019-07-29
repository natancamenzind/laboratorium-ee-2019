# Generated by Django 2.2.2 on 2019-06-25 12:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20190618_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='process',
            field=wagtail.core.fields.StreamField([('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='process_en',
            field=wagtail.core.fields.StreamField([('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='process_pl',
            field=wagtail.core.fields.StreamField([('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
    ]