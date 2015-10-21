from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime

from .models import Video

def index(request, page_number=1):

    items_per_page = 4
    query_set = Video.objects.all().order_by('published_date')
    paginator = Paginator(query_set, items_per_page)
    base_url = reverse('videos:index')

    try:
        current_page = paginator.page(page_number)
        has_next = current_page.has_next()
        next_page_number = None
        if current_page.has_next():
            next_page_number = current_page.next_page_number()
    except InvalidPage:
        raise Http404

    return render_to_response('videos/index.tmpl.html',
                              {'current_page': current_page,
                               'has_next_page' : has_next,
                               'next_page_number' : next_page_number,
                               'base_url': base_url},
                              context_instance=RequestContext(request))

def detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    base_url = reverse('videos:index')

    try:
        next_item = video.get_next_by_published_date()
    except Video.DoesNotExist:
        next_item = False

    try:
        previous_item = video.get_previous_by_published_date()
    except Video.DoesNotExist:
        previous_item = False

    return render_to_response('videos/detail.tmpl.html',
                              {'video': video,
                               'base_url': base_url,
                               'previous_item': previous_item,
                               'next_item': next_item,
                               'verbose_name': Video._meta.verbose_name,
                               'current_url': request.build_absolute_uri(request.path)},
                              context_instance=RequestContext(request))

