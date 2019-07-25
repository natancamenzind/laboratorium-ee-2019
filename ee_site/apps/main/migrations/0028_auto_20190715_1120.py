# Generated by Django 2.2.3 on 2019-07-15 09:20

from django.db import migrations
import ee_site.apps.main.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20190712_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpage',
            name='content',
            field=wagtail.core.fields.StreamField([('contact_form', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('form_heading', wagtail.core.blocks.CharBlock(required=False))])), ('contact_us_button', ee_site.apps.main.blocks.ContactUsButtonBlock()), ('hero_process', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('headline', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], required=False)), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))])), ('hero_static_right', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('headline', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('page_secodary', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False))])), ('masonry', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('featured_x', wagtail.core.blocks.BooleanBlock(required=False)), ('featured_y', wagtail.core.blocks.BooleanBlock(required=False)), ('featured_mobile', wagtail.core.blocks.BooleanBlock(required=False)), ('title_dark', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])), ('quote', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'])), ('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], required=False))])), ('tile_grid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))])), ('tile_grid_spaced', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='subpage',
            name='content_en',
            field=wagtail.core.fields.StreamField([('contact_form', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('form_heading', wagtail.core.blocks.CharBlock(required=False))])), ('contact_us_button', ee_site.apps.main.blocks.ContactUsButtonBlock()), ('hero_process', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('headline', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], required=False)), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))])), ('hero_static_right', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('headline', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('page_secodary', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False))])), ('masonry', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('featured_x', wagtail.core.blocks.BooleanBlock(required=False)), ('featured_y', wagtail.core.blocks.BooleanBlock(required=False)), ('featured_mobile', wagtail.core.blocks.BooleanBlock(required=False)), ('title_dark', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])), ('quote', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'])), ('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], required=False))])), ('tile_grid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))])), ('tile_grid_spaced', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subpage',
            name='content_pl',
            field=wagtail.core.fields.StreamField([('contact_form', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('form_heading', wagtail.core.blocks.CharBlock(required=False))])), ('contact_us_button', ee_site.apps.main.blocks.ContactUsButtonBlock()), ('hero_process', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('headline', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], required=False)), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))])), ('hero_static_right', wagtail.core.blocks.StructBlock([('background_image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('headline', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock()), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('page_secodary', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False))])), ('masonry', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('page', wagtail.core.blocks.PageChooserBlock()), ('featured_x', wagtail.core.blocks.BooleanBlock(required=False)), ('featured_y', wagtail.core.blocks.BooleanBlock(required=False)), ('featured_mobile', wagtail.core.blocks.BooleanBlock(required=False)), ('title_dark', wagtail.core.blocks.BooleanBlock(required=False))])))])), ('paragraph', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])), ('quote', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'])), ('author', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], required=False))])), ('tile_grid', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))])), ('tile_grid_spaced', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('tiles', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('subtitle', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link']))])))]))], blank=True, null=True),
        ),
    ]
