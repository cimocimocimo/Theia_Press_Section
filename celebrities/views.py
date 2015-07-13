from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.core.urlresolvers import reverse

from celebrities.models import Celebrity, Dress

# Create your views here.
def index(request, page_number=1):

    items_per_page = 12
    query_set = Celebrity.objects.all()
    featured_celebrity = False
    if query_set.exists():
        featured_celebrity = query_set[:1].get()
    paginator = Paginator(query_set[1:], items_per_page)
    base_url = reverse('celebrities:index')

    try:
        current_page = paginator.page(page_number)
        has_next = current_page.has_next()
        next_page = current_page.number + 1
    except InvalidPage:
        raise Http404

    return render_to_response('celebrities/index.tmpl.html',
                              {'current_page': current_page, 'has_next' : has_next, 'next_page' : next_page, 'featured_celebrity': featured_celebrity, 'base_url': base_url},
                              context_instance=RequestContext(request))

def celeb_detail(request, slug):
    celeb = get_object_or_404(Celebrity, slug=slug)
    dresses = Dress.objects.filter(celebrity=celeb)
    return render_to_response('celebrities/celeb_detail.tmpl.html',
                              {'celebrity': celeb, 'dresses': dresses},
                              context_instance=RequestContext(request))

def dress_detail(request, celeb_slug, dress_slug):
    celeb = get_object_or_404(Celebrity, slug=celeb_slug)
    dress = get_object_or_404(Dress, slug=dress_slug)
    dresses = Dress.objects.filter(celebrity=celeb)
    return render_to_response('celebrities/dress_detail.tmpl.html',
                              {'celebrity': celeb, 'dress': dress, 'dresses': dresses},
                              context_instance=RequestContext(request))
