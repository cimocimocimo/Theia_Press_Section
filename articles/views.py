from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from articles.models import Article

def index(request):
    latest_articles = Article.objects.order_by('-published_date')[:5]

    return render_to_response('articles/index.html',
                              {'latest_articles': latest_articles},
                              context_instance=RequestContext(request))

def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render_to_response('articles/detail.html',
                              {'article': article},
                              context_instance=RequestContext(request))
