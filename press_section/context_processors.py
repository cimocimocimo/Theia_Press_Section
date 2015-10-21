from django.core.urlresolvers import resolve
from django.conf import settings

def appname(request):
    try:
        app_name = request.resolver_match.app_name
    except AttributeError:
        app_name = None

    return {'appname': app_name}

def shopify(request):
    try:
        shop_name = settings.SHOPIFY_SHOP_NAME
    except AttributeError:
        shop_name = None

    return {'shopify_shop_name': shop_name}
