from django.shortcuts import render
from django.conf import settings
from django.urls import URLPattern, URLResolver, reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Profile
from manage_links.models import Link, SocialMedia

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
    URL config: /
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

class UserProfileDetailView(DetailView):
    """
    Detail view for a user profile
    URL config: /profile/<username>/
    """

    model = Profile
    context_object_name = "user_profile"
    template_name = "manage_users/profile_detail.html"

    # Get user profile to display from username parameter in URL
    def get_object(self, **kwargs):
        _username = self.kwargs["username"]
        user_to_display = User.objects.get(username=_username)
        return Profile.objects.get(user=user_to_display)

    # Get links associated with user profile and currently logged in user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user # Currently logged in user
        # Get links associated with user profile
        user_to_display = User.objects.get(username=self.kwargs["username"])
        links = Link.objects.filter(user=user_to_display)
        socials = SocialMedia.objects.filter(user=user_to_display)
        print(links)
        print(socials)
        context['urls'] = links
        context['socials'] = socials
        return context


class UserProfileRedirectView(RedirectView):
    """
    Redirect view for a user profile with URL pattern "/accounts/profile"
    Redirect to the profile of the current logged in user if logged in, homepage otherwise.
    URL config: /accounts/profile/ => /profile/<username>/
    """
    pattern_name = "profile-detail"

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            return reverse(
                self.pattern_name,
                kwargs={"username": self.request.user.username},
            )
        else:
            return reverse("index")

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for a user profile
    Only accessible when logged in
    URL config: /profile/update/
    """
    model = Profile
    fields = ["display_name", "bio", "profile_photo", "background_photo"]
    template_name = "manage_users/profile_update.html"

    # Get user profile to update
    def get_object(self, **kwargs):
        user = self.request.user
        return Profile.objects.get(user=user)

    # Get current logged in user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

    # Redirect to the profile of the current logged in user
    def get_success_url(self):
        return reverse(
            "profile-detail",
            kwargs={"username": self.request.user.username},
        )