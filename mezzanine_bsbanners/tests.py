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
from django.test import TestCase
from django.template import Template, Context, TemplateSyntaxError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from mezzanine_bsbanners.models import Banners, Slides

#pylint: disable=too-many-public-methods
class BSBannersTestCase(TestCase):
    """
    Class to test mezzanine_bsbanners
    """
    def setUp(self):
        """
        Setup test
        """
        Banners.objects.create(title="Home")
        Banners.objects.create(title="Home Carousel", bannertype=1)
        jumbo = Banners.objects.create(
            title="Home Jumbotron",
            bannertype=2,
        )
        #pylint: disable=no-member
        Slides.objects.create(
            banner_id=jumbo.id,
            title='Jumbotrons are GREAT!',
            content='<p>Bootstrap Jumbotrons are great headline grabbers</p>',
            cta='Get one today',
            link_url='http://p-o.co.uk/',
            buttontype='default'
        )
        #pylint: enable=no-member

    def test_banner_has_good_slug(self):
        """Banners should have the correct slugs"""
        homebanner = Banners.objects.get(title="Home")
        homecarousel = Banners.objects.get(title="Home Carousel")
        homejumbo = Banners.objects.get(title="Home Jumbotron")
        self.assertEqual(homebanner.title, 'Home')
        self.assertEqual(homebanner.slug, 'home')
        self.assertEqual(homecarousel.title, 'Home Carousel')
        self.assertEqual(homecarousel.slug, 'home-carousel')
        self.assertEqual(homejumbo.title, 'Home Jumbotron')
        self.assertEqual(homejumbo.slug, 'home-jumbotron')

    def test_get_carousel_bsbanner(self):
        """
        Test carousel rendering
        """
        out = Template(
            '{% load bsbanners_tags %}'
            '{% bsbanner "home" %}'
        ).render(Context())
        pagedat = """


<script type='text/javascript'>
window.setTimeout(function()
{
    // Prepare the carousel
    var carousel7options = {
        interval: 5000,
        pause: "hover",
        wrap: true,
    }
    jQuery('#home-carousel .carousel-caption').hide();
    jQuery('#home-carousel .active .carousel-caption').show();
    // Activate the carousel
    jQuery('.carousel').carousel(carousel7options);

    // Set the carousel animations
    jQuery('.carousel').on('slide.bs.carousel', function() {
        jQuery('#home-carousel .active .carousel-caption').slideUp(500);
    });
    jQuery('.carousel').on('slid.bs.carousel', function() {
        jQuery('#home-carousel .active .carousel-caption').slideDown(300);
    });

}, 5000);
</script>


<!-- Carousel
================================================== -->
<div id='home-carousel' class="carousel slide">
    <div class="carousel-inner">
    
    </div>
    <a class="left carousel-control" href="#home-carousel" data-slide="prev">&lsaquo;</a>
    <a class="right carousel-control" href="#home-carousel" data-slide="next">&rsaquo;</a>
    
    <ul class="carousel-indicators">
    
    </ul>
    
</div><!-- /.carousel -->


"""
        self.assertEqual(out, pagedat)

    def test_get_jumbotron_bsbanner(self):
        """
        Test jumbotron rendering
        """
        out = Template(
            '{% load bsbanners_tags %}'
            '{% bsbanner "home-jumbotron" %}'
        ).render(Context())
        pagedat = """


<div id='home-jumbotron-jumbotron' class="jumbotron">
    <div class="container">
    
        <div>
        
            <h1>Jumbotrons are GREAT!</h1>
        
        <p>Bootstrap Jumbotrons are great headline grabbers</p>
        
            
            <a class="btn btn-default"
                href="http://p-o.co.uk/">
            
            
            Get one today
            
            
            </a>
            
        
        </div>
    
    </div>
</div>


"""
        self.assertEqual(out, pagedat)

    def test_banner_found_failures(self):
        """
        Non existent banners should barf as well as too many
        """

        self.assertRaises(MultipleObjectsReturned, Banners.objects.get)
        self.assertRaises(ObjectDoesNotExist, Banners.objects.get, title="zzz")
        self.assertRaisesMessage(
            ObjectDoesNotExist,
            'Banners matching query does not exist.',
            Banners.objects.get,
            title="azerty")

    def test_parsing_errors(self):
        "Parsing variation on template"
        #    {% bsbanner {block} %}
        #    {% bsbanner {block} {template_name} %}
        render = lambda t: Template(t).render(Context())

        self.assertRaises(
            TemplateSyntaxError, render,
            "{% load bsbanners_tags %}{% bsbanner %}")
        self.assertRaises(
            TemplateSyntaxError, render,
            "{% load bsbanners_tags %}{% bsbanner 'one' 'two' 'three' %}")
        self.assertRaises(
            TemplateSyntaxError, render,
            "{% load bsbanners_tags %}{% bsbanner one two three four five %}")
