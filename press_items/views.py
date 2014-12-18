from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from press_items.models import PressItem

# Create your views here.

def index(request, item_filter):
    # **TODO** filter by press item type
    if item_filter is not None:
        latest_press_items = PressItem.objects.filter(item_type__slug=item_filter)
    else: 
        latest_press_items = PressItem.objects.order_by('-published_date')[:5]

    return render_to_response('press_items/index.html',
                              {'latest_press_items': latest_press_items},
                              context_instance=RequestContext(request))

def detail(request, slug):
    item = get_object_or_404(PressItem, slug=slug)
    return render_to_response('press_items/detail.html',
                              {'item': item},
                              context_instance=RequestContext(request))
