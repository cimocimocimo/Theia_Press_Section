from django.core.urlresolvers import resolve

def appname(request):
    return {'appname': request.resolver_match.app_name}
