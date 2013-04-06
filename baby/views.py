from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from baby.models import Baby, RsvpForm, Rsvp, Article
from django.http import HttpResponse
from datetime import *
import prego
import urllib2

#index
def index(request):
    prego_dates = prego.Prego(datetime(2012, 7, 18, 12, 0), datetime.now())
    current_weeks = prego_dates.getWeeks()
    baby = Baby.objects.get(week = current_weeks)

    form = RsvpForm()
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def rsvp(request):

    if request.is_ajax() or request.method == 'POST':
        form = RsvpForm(data = request.POST)
        if form.is_valid():
            name = request.POST.get('name', False)
            coming = request.POST.get('coming', False)
            if coming == 'yes':
                coming = True
            else:
                coming = False
            rsvp = Rsvp(name = name, coming = coming)
            rsvp.save()
            return HttpResponse(coming)
        else:
            return HttpResponse('false')

def get_article(request, slug):
    article = get_object_or_404(Article, slug = slug)
    #slug = request.get_full_path().split('/')[2]


    return render_to_response(slug + '.html', locals(),
        context_instance = RequestContext(request))


def get_instagram(request):
    tag = 'alicesadwick2013'
    req = urllib2.Request("https://api.instagram.com/v1/tags/" + tag + "/media/recent?access_token=5555021.f59def8.f51d43b3e8614db18ff57566d8f3f839&count=50")
    opener = urllib2.build_opener()
    instagram = opener.open(req)
    json = simplejson.load(instagram)
    images = []
    for image in json['data']:
        images.append({'thumbnail' : image['images']['thumbnail'], 'standard' : image['images']['standard_resolution'], 'caption' : image['caption'] })

    return HttpResponse(simplejson.dumps(images), mimetype = 'text/json')