from django.shortcuts import render
from django.conf import settings
from django.urls import URLPattern, URLResolver

# Getting a list of all url configs in the app
# From:
# https://stackoverflow.com/questions/1275486/django-how-can-i-see-a-list-of-urlpatterns


def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])
    yield from list_urls(lis[1:], acc)


# Create your views here.
def index(request):
    """
    Index page with all URLs in the project
    """
    urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [""])
    urls = []
    context_dict = {}
    for p in list_urls(urlconf.urlpatterns):
        url = "".join(p)
        if "admin" not in url:
            urls.append(url)
    context_dict["urls"] = urls

    return render(request, "index.html", context_dict)
