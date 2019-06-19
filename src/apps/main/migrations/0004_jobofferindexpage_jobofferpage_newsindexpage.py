# Generated by Django 2.2.1 on 2019-05-24 14:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('main', '0003_newspage'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOfferIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('cooperation', models.CharField(max_length=500)),
                ('cooperation_pl', models.CharField(max_length=500, null=True)),
                ('cooperation_en', models.CharField(max_length=500, null=True)),
                ('recruitment', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))])),
                ('recruitment_pl', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))], null=True)),
                ('recruitment_en', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('tiles_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='JobOfferPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('salary', models.CharField(max_length=50)),
                ('employment_form', models.CharField(max_length=50)),
                ('body', wagtail.core.fields.RichTextField()),
                ('body_pl', wagtail.core.fields.RichTextField(null=True)),
                ('body_en', wagtail.core.fields.RichTextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
