from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models import Event, EventsConfig

def index(request, page_number=1):

    items_per_page = 4
    query_set = Event.objects.order_by('-from_datetime')
    paginator = Paginator(query_set, items_per_page)
    base_url = reverse('events:index')
    events_config = EventsConfig.get_solo()

    try:
        current_page = paginator.page(page_number)
        has_next = current_page.has_next()
        next_page_number = None
        if current_page.has_next():
            next_page_number = current_page.next_page_number()
    except InvalidPage:
        raise Http404

    return render_to_response('events/index.tmpl.html',
                              {'current_page': current_page,
                               'has_next_page' : has_next,
                               'next_page_number' : next_page_number,
                               'base_url': base_url,
                               'events_config': events_config},
                              context_instance=RequestContext(request))

def detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    base_url = reverse('events:index')
    
    try:
        next_item = event.get_next_by_from_datetime()
    except Event.DoesNotExist:
        next_item = False

    try:
        previous_item = event.get_previous_by_from_datetime()
    except Event.DoesNotExist:
        previous_item = False
        
    return render_to_response('events/detail.tmpl.html',
                              {'event': event,
                               'location_hours': condense_opening_hours(
                                   event.eventlocationhours_set.order_by('weekday').all()),
                               'base_url': base_url,
                               'previous_item': previous_item,
                               'next_item': next_item,
                               'verbose_name': Event._meta.verbose_name,
                               'current_url': request.build_absolute_uri(request.path)},
                              context_instance=RequestContext(request))

def condense_opening_hours(hours):
    """
    Condenses the days open with identical times to a range of days.
    """
    weekdays = (
        "",
        "Mo",
        "Tu",
        "We",
        "Th",
        "Fr",
        "Sa",
        "Su",
    )
    
    hours_condensed = []
    for index, open_time in enumerate(hours):
        if index == 0:
            hours_condensed.append(
                {
                    'day': [open_time.weekday,],
                    'from': open_time.from_hour,
                    'to': open_time.to_hour,
                }
            )
        else:
            previous_hours = hours[index - 1]
            if previous_hours.from_hour == open_time.from_hour and previous_hours.to_hour == open_time.to_hour:
                # yesterday's hours are itentical, we can condense the two days into one
                hours_condensed[-1]['day'].append(open_time.weekday)
            else:
                hours_condensed.append(
                    {
                        'day': [open_time.weekday,],
                        'from': open_time.from_hour,
                        'to': open_time.to_hour,
                    }
                )

    for index, hours in enumerate(hours_condensed):
        if len(hours['day']) > 1:
            hours_condensed[index]['day'] = '{} - {}'.format(weekdays[hours['day'][0]], weekdays[hours['day'][-1]])
        else:
            hours_condensed[index]['day'] = weekdays[hours['day'][0]]
    return hours_condensed
