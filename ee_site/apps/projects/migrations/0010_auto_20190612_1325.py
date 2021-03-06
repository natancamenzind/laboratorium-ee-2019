# Generated by Django 2.2.2 on 2019-06-12 11:25

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('projects', '0009_auto_20190603_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='specializationpage',
            name='background_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='specializationpage',
            name='short_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specializationpage',
            name='short_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='specializationpage',
            name='short_description_pl',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='specializationpage',
            name='case_study',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
        migrations.AlterField(
            model_name='specializationpage',
            name='case_study_en',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
        migrations.AlterField(
            model_name='specializationpage',
            name='case_study_pl',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
        migrations.AlterField(
            model_name='specializationpage',
            name='how_we_work',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))]),
        ),
        migrations.AlterField(
            model_name='specializationpage',
            name='how_we_work_en',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
        migrations.AlterField(
            model_name='specializationpage',
            name='how_we_work_pl',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]), template='projects/blocks/tiles_list.html'))], null=True),
        ),
    ]
