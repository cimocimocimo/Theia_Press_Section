from django.core.urlresolvers import resolve
from django.contrib.sites.models import Site
from django.conf import settings

def appname(request):
    try:
        app_name = request.resolver_match.app_name
    except AttributeError:
        app_name = None

    return {'appname': app_name}

def site_domain(request):
    current_site = Site.objects.get_current()
    return {'site_domain': current_site.domain}

# returns the main shop url for use in navigation and to show users
def shopify_settings(request):

    # TODO: Add error check to this context processor
    # try:
    #     shop_name = settings.SHOPIFY_SHOP_NAME
    # except AttributeError:
    #     shop_name = None

    # return {'shopify_shop_name': shop_name}

    # TODO: Create a dict for the SHOPIFY settings
    # that would allow for simpler error checking
    return {
        'shopify': {
            'shop_url': settings.SHOPIFY_SHOP_URL,
            'shop_domain': settings.SHOPIFY_SHOP_DOMAIN
        }
    }
