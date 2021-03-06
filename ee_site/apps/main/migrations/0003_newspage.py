# Generated by Django 2.2.1 on 2019-05-23 16:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('main', '0002_auto_20190515_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=500)),
                ('headline_pl', models.CharField(max_length=500, null=True)),
                ('headline_en', models.CharField(max_length=500, null=True)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('body', wagtail.core.fields.RichTextField()),
                ('body_pl', wagtail.core.fields.RichTextField(null=True)),
                ('body_en', wagtail.core.fields.RichTextField(null=True)),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
