from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.conf import settings

from mtlpy.shortener.models import Shortcut
from mtlpy.shortener.forms import ShortcutForm

def short(request, slug):
    try:
        link = Shortcut.objects.get(slug=slug).link
    except:
        link = settings.FALLBACK_URL + slug

    return redirect(link, permanent=True)


def index(request):
    if request.method == "POST":
        form = ShortcutForm(request.POST)
        if form.is_valid():
            link = form.save()
            if len(link.slug) == 0:
                link = Shortcut.objects.get(link = link.link)
            return redirect('mtlpy.shortener.views.detail', link.slug)
    else:
        form = ShortcutForm()
    return render_to_response("index.html", {'form': form})

def detail(request, slug=''):
    link = get_object_or_404(Shortcut, slug=slug)
    return render_to_response("detail.html", {'shortcut': link})

def json(request):
    if request.method == "POST":
        link = request.POST.get("link")
    else:
        link = request.GET.get("link")
        print simplejson.dumps({'result': 'success', 'link': link, 'url': 'lolz'})
        #fail
        pass
