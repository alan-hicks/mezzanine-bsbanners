#----------------------------------------------------------------------
# Copyright (c) 2014, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
Mezzanine BS Banners
Making it easier to manage attention grabbing and compelling banners
"""

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mezzanine_bsbanners.models import Banners, Slides

class SlidesInline(admin.StackedInline):
    """
    Inline Slides Admin class
    """
    model = Slides
    extra = 1

    fieldsets = (
        (None, {
            "fields": [
                'title', 'show_title',
                'content',
                'cta', 'buttontype',
                'image', 'link_url',
                'status'
            ],
        }),
    )

class BannersAdmin(admin.ModelAdmin):
    """
    Admin class for Banners
    """
    #pylint: disable=too-many-public-methods
    list_display = ('title', 'slug', 'status', )
    list_editable = ('status', )

    fieldsets = (
        (None, {
            "fields": ["title", 'bannertype'],
        }),
        (_("Advanced data"), {
            "fields": ['slug',
                       'buttonsize', 'ctachevron',
                       'interval', 'wrap', 'pause',
                       'showindicators', 'animate',
                       'status'],
            "classes": ("collapse-closed",)
        }),
    )

    inlines = [
        SlidesInline,
    ]

admin.site.register(Banners, BannersAdmin)
