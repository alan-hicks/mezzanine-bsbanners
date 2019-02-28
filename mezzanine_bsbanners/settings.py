#----------------------------------------------------------------------
# Copyright (c) 2014-2019, Persistent Objects Ltd https://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
Settings for Mezzanine BS Banners
"""

# django imports
from django.conf import settings

# PATH AND URL SETTINGS

# Main Media Settings
MEDIA = getattr(settings, "BSBANNERS_MEDIA", 'slides/')
