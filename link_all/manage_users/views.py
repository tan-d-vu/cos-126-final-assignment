from django.shortcuts import render
from django.conf import settings
from django.urls import URLPattern, URLResolver, reverse
from django.views.generic import DetailView, RedirectView
from django.contrib.auth.models import User
from .models import Profile

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


# TODO: Implement the following views:
# SIMPLE_BACKEND_REDIRECT_URL = '/accounts/update/' # Redirect to this URL after registration.
# LOGIN_REDIRECT_URL = '/profile/' # Redirect to this URL after login.
class UserProfileDetailView(DetailView):
    """
    Detail view for a user profile
    """

    model = Profile
    context_object_name = "user_profile"
    template_name = "manage_users/profile_detail.html"

    # Get user profile to display from username parameter in URL
    def get_object(self, **kwargs):
        _username = self.kwargs["username"]
        user_to_display = User.objects.get(username=_username)
        return Profile.objects.get(user=user_to_display)

    # Get current logged in user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context


class UserProfileRedirectView(RedirectView):
    """
    Redirect view for a user profile when <username> is not given.
    Redirect to the profile of the current logged in user if logged in, homepage otherwise.

    """

    pattern_name = "profile-detail"

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse(
                self.pattern_name,
                kwargs={"username": self.request.user.username},
            )
        else:
            return reverse("index")
