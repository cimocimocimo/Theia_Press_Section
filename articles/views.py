from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.core.urlresolvers import reverse

from articles.models import Article

def index(request, page_number=1):

    items_per_page = 8
    query_set = Article.objects.order_by('-original_publication_date')
    paginator = Paginator(query_set, items_per_page)
    base_url = reverse('articles:index')

    try:
        current_page = paginator.page(page_number)
        has_next = current_page.has_next()
        next_page_number = None
        if current_page.has_next():
            next_page_number = current_page.next_page_number()
    except InvalidPage:
        raise Http404

    return render_to_response('articles/index.tmpl.html',
                              {'current_page': current_page,
                               'has_next_page' : has_next,
                               'next_page_number' : next_page_number,
                               'base_url': base_url},
                              context_instance=RequestContext(request))

def index_by_tag(request, tag, page_number=1):

    items_per_page = 8
    query_set = Article.objects.filter(tags__slug__in=[tag]).distinct().order_by('-original_publication_date')
    paginator = Paginator(query_set, items_per_page)
    base_url = reverse('articles:index_by_tag', kwargs={'tag': tag})

    try:
        current_page = paginator.page(page_number)
        has_next = current_page.has_next()
        next_page_number = None
        if current_page.has_next():
            next_page_number = current_page.next_page_number()
    except InvalidPage:
        raise Http404

    return render_to_response('articles/index.tmpl.html',
                              {'current_page': current_page,
                               'has_next_page' : has_next,
                               'next_page_number' : next_page_number,
                               'base_url': base_url},
                              context_instance=RequestContext(request))


def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    base_url = reverse('articles:index')

    try:
        next_item = article.get_next_by_original_publication_date()
    except Article.DoesNotExist:
        next_item = False

    try:
        previous_item = article.get_previous_by_original_publication_date()
    except Article.DoesNotExist:
        previous_item = False

    return render_to_response('articles/detail.tmpl.html',
                              {'article': article,
                               'base_url': base_url,
                               'previous_item': previous_item,
                               'next_item': next_item,
                               'verbose_name': Article._meta.verbose_name},
                              context_instance=RequestContext(request))
