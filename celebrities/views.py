from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import RequestContext

from celebrities.models import Celebrity, Dress

# Create your views here.
def index(request):
    celebs = Celebrity.objects.all()
    return render_to_response('celebrities/index.html',
                              {'celebrities': celebs},
                              context_instance=RequestContext(request))

def celeb_detail(request, slug):
    celeb = get_object_or_404(Celebrity, slug=slug)
    dresses = Dress.objects.filter(celebrity=celeb)
    return render_to_response('celebrities/celeb_detail.html',
                              {'celebrity': celeb, 'dresses': dresses},
                              context_instance=RequestContext(request))

def dress_detail(request, celeb_slug, dress_slug):
    celeb = get_object_or_404(Celebrity, slug=celeb_slug)
    dress = get_object_or_404(Dress, slug=dress_slug)
    dresses = Dress.objects.filter(celebrity=celeb)
    return render_to_response('celebrities/dress_detail.html',
                              {'celebrity': celeb, 'dress': dress, 'dresses': dresses},
                              context_instance=RequestContext(request))
