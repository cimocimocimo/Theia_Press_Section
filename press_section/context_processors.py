from django.core.urlresolvers import resolve

def appname(request):
    try:
        app_name = request.resolver_match.app_name
    except AttributeError:
        app_name = None

    return {'appname': app_name}
