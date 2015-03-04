from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.core.urlresolvers import reverse

from events.models import Event

def index(request, page_number=1):

    items_per_page = 4
    query_set = Event.objects.order_by('event_date')
    paginator = Paginator(query_set, items_per_page)
    base_url = reverse('events:index')

    try:
        current_page = paginator.page(page_number)
    except InvalidPage:
        raise Http404

    return render_to_response('events/index.tmpl.html',
                              {'current_page': current_page, 'base_url': base_url},
                              context_instance=RequestContext(request))

def detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    base_url = reverse('events:index')
    

    try:
        next_item = event.get_next_by_event_date()
    except Event.DoesNotExist:
        next_item = False

    try:
        previous_item = event.get_previous_by_event_date()
    except Event.DoesNotExist:
        previous_item = False

    return render_to_response('events/detail.tmpl.html',
                              {'event': event,
                               'base_url': base_url,
                               'previous_item': previous_item,
                               'next_item': next_item,
                               'verbose_name': Event._meta.verbose_name,
                               'current_url': request.build_absolute_uri(request.path)},
                              context_instance=RequestContext(request))
