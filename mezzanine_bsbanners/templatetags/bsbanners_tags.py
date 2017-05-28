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
from django import template
from django.template import loader
from mezzanine_bsbanners.models import Banners
from mezzanine.conf import settings

#pylint: disable=invalid-name
register = template.Library()
#pylint: enable=invalid-name

#pylint: disable=too-few-public-methods
class BSBannerBlockWrapper(object):
    """
    Wrapper class to render a BS Banner block
    """
    slug = None
    template_name = None

    def prepare(self, parser, token):
        """
        The parser checks for following tag invocations:
            {% bsbanner {URL} %}
            {% bsbanner {URL} {template_name} %}
        """
        #pylint: disable=unused-argument
        msg = "%r tag should have between 1 and 2 arguments \
        for slug of banner to display and optional template"
        tokens = token.split_contents()
        self.slug = None
        self.template_name = None
        if len(tokens) < 2:
            raise template.TemplateSyntaxError(msg % (tokens[0],))
        if len(tokens) > 3:
            raise template.TemplateSyntaxError(msg % (tokens[0],))

        self.slug = tokens[1]
        if len(tokens) == 3:
            self.template_name = tokens[2]

        # Resolve the slug if it is a variable
        if self.slug[0] in ('"', "'"):
            self.slug = self.slug[1:-1]
        else:
            self.slug = template.Variable(self.slug)

        # Resolve the template name
        if self.template_name is None:
            self.template_name = 'bsbanners/banner.html'
        elif self.template_name[0] in ('"', "'"):
            self.template_name = self.template_name[1:-1]
        else:
            self.template_name = template.Variable(self.template_name)

    def __call__(self, parser, token):
        self.prepare(parser, token)
        return BSBannerBlockNode(self.slug, template_name=self.template_name)

#pylint: disable=invalid-name
do_bsbannerblock = BSBannerBlockWrapper()
#pylint: enable=invalid-name

class BSBannerBlockNode(template.Node):
    """
    Get a block node
    """
    def __init__(self, slug, template_name=None):

        self.slug = slug
        self.template_name = template_name

    def render(self, context):
        try:
            if isinstance(self.slug, template.Variable):
                self.slug = self.slug.resolve(context)

            bsbannerblock = Banners.objects.get(
                slug=self.slug,
                status=2,
            )

            slides = []
            isfirst = True
            qry_slides = bsbannerblock.slides_set.filter(
                status=2
            ).order_by("sort_order")
            for slide in qry_slides:
                slide.isfirst = isfirst
                isfirst = False
                slides.append(slide)

            tmpl = loader.get_template(self.template_name)
            new_context = {
                'bsbannerblock':bsbannerblock,
                'slides':slides,
                'MEDIA_URL':settings.MEDIA_URL,
                }

            return tmpl.render(new_context)
        #pylint: disable=no-member
        except Banners.DoesNotExist:
        #pylint: enable=no-member
            return ''

register.tag('bsbanner', do_bsbannerblock)
