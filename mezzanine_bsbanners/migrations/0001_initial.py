# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('bannertype', models.SmallIntegerField(default=1, choices=[(1, 'Carousel'), (2, 'Jumbotron')])),
                ('ctachevron', models.CharField(default='none', help_text='Add a chevron to call to action buttons', max_length=5, verbose_name='Button chevrons', choices=[('none', 'None'), ('left', 'Left'), ('right', 'Right')])),
                ('buttonsize', models.CharField(default='default', help_text='Size of call to action buttons', max_length=7, verbose_name='Button size', choices=[('lg', 'Large'), ('default', 'Default'), ('sm', 'Small'), ('xs', 'Extra small')])),
                ('interval', models.IntegerField(default=5000, help_text='The amount of time (in milliseconds) to delay between automatically cycling an item', verbose_name='interval')),
                ('wrap', models.BooleanField(default=True, help_text='Whether the carousel should cycle continuously or have hard stops', verbose_name='wrap')),
                ('pause', models.BooleanField(default=True, help_text='Pauses the cycling of the carousel on mouseenter and resumes the cycling of the carousel on mouseleave', verbose_name='pause')),
                ('showindicators', models.BooleanField(default=True, verbose_name='Show indicators')),
                ('animate', models.BooleanField(default=True, verbose_name='Animate transitions')),
                ('status', models.SmallIntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Slides',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('title', models.CharField(help_text='Slide/Jumbotron title', max_length=200, verbose_name='Title')),
                ('show_title', models.BooleanField(default=True, help_text='If checked, show slide/jumbotron title.', verbose_name='Show title')),
                ('cta', models.CharField(help_text='Text used for the call to action button', max_length=200, null=True, verbose_name='Call to action', blank=True)),
                ('link_url', models.CharField(help_text='Link for the image and call to action button', max_length=200, null=True, verbose_name='Link', blank=True)),
                ('buttontype', models.CharField(default='default', help_text='Call to action button type (colour)', max_length=7, verbose_name='Button type', choices=[('default', 'default'), ('primary', 'primary'), ('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('danger', 'danger')])),
                ('image', models.FileField(max_length=255, upload_to=b'slides/', null=True, verbose_name='Image', blank=True)),
                ('status', models.SmallIntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('sort_order', models.SmallIntegerField(editable=False)),
                ('banner', models.ForeignKey(to='mezzanine_bsbanners.Banners')),
            ],
            options={
                'ordering': ['sort_order'],
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
    ]
