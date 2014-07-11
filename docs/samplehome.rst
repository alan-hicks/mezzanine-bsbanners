Sample home page template
=========================

This example shows how a simple home page template can be created using a
normal Mezzanine page.  It uses most of the information including title,
keywords, description and content from a normal Mezzanine page with a carousel
or jumbotron banner making it easy to manage without editing the template.

urls.py::

    urlpatterns = patterns("",
        # Home page
        url(r"^$", views.home, name="home"),
        ...
    )

views.py::

    def home(request):
        """
        Home page request
        """
        page = Page.objects.get(slug='/')
        context = {
            "page": page,
        }
        return render(request, 'myapp/home.html', context)

home.html::

    {% extends "base.html" %}
    {% load staticfiles mezzanine_tags keyword_tags bsbanners_tags %}

    {% block meta_title %}{{ page.meta_title }}{% endblock %}

    {% block meta_keywords %}{% metablock %}
    {% keywords_for page as keywords %}
    {% for keyword in keywords %}
        {% if not forloop.first %}, {% endif %}
        {{ keyword }}
    {% endfor %}
    {% endmetablock %}{% endblock %}

    {% block meta_description %}{% metablock %}
    {{ page.description }}
    {% endmetablock %}{% endblock %}

    {% block title %}
    {{ page.title }}
    {% endblock %}

    {% block main %}
    <div id="content" class="col-md-12">

        {% bsbanner "home-banner" %}

        <div>
        {{ page.myapp.content|safe }}
        </div>

    </div>
    {% endblock %}