====================
Mezzanine BS Banners
====================

**Making it easier to manage attention grabbing Bootstrap Carousels and
compelling Bootstrap Jumbotrons as banners on home pages**

Designed to quickly and easily manange attention grabbing Bootstrap carousels
and compelling Bootstrap Jumbotrons as banners with the same ease as ordinary
Mezzanine pages without editing templates.

The following Bootstrap layouts are supported:

* Carousel
* Jumbotron

Quick start
-----------

1. Install the app

2. Add "mezzanine_bsbanners" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mezzanine_bsbanners',
    )

3. Add blocks menu item to admin menu (Optional)::

    ADMIN_MENU_ORDER = (
        ("Content", (
                "mezzanine_bsbanners.*",
            )
        ),
    )


3. Run 'python manage.py syncdb' to create the database models.

Usage
=====
mezzanine-bsbanners are similar to django-flatblocks.

1. Include bsbanners_tags in the template::

    {% load ... bsbanners_tags %}

2. Insert block anywhere in the template::

    {% bsbanner "My Banner" %}
    {% bsbanner {block} %}
    {% bsbanner {block} "my_template.html" %}
    {% bsbanner {block} {template_name} %}

Dependencies
============

* `Django`_ 1.6
* `Mezzanine`_ 3.x
* `Bootstrap`_ 3.x

Support
=======

To report a security issue, please send an email privately to
`ahicks@p-o.co.uk`_. This gives us a chance to fix the issue and
create an official release prior to the issue being made
public.

For general questions or comments, please contact  `ahicks@p-o.co.uk`_.

`Project website`_

Communications are expected to conform to the `Django Code of Conduct`_.

.. GENERAL LINKS

.. _`Bootstrap`: http://getbootstrap.com/
.. _`Django`: http://djangoproject.com/
.. _`Django Code of Conduct`: https://www.djangoproject.com/conduct/
.. _`Python`: http://python.org/
.. _`Persistent Objects Ltd`: http://p-o.co.uk/
.. _`Project website`: http://p-o.co.uk/tech-articles/mezzanine-bootstrap-banners/
.. _`Mezzanine`: http://mezzanine.jupo.org


.. PEOPLE WITH QUOTES

.. _`Alan Hicks`: https://plus.google.com/103014117568943351106
.. _`ahicks@p-o.co.uk`: mailto:ahicks@p-o.co.uk?subject=mezzanine-bsbanners+Security+Issue
