from django.core.urlresolvers import resolve
from django.contrib.sites.models import Site

def appname(request):
    try:
        app_name = request.resolver_match.app_name
    except AttributeError:
        app_name = None

    return {'appname': app_name}

def site_domain(request):
    current_site = Site.objects.get_current()
    return {'site_domain': current_site.domain}
