from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Link, SocialMedia


class ManageLinksMixin:
    """
    Mixin containing common methods for all views in app manage_links
    """

    def form_valid(self, form):
        """
        Add ForeignKey relationship between new link and current logged in user
        """
        """
        Task: Add ForeignKey relationship between new link and current logged in user
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Add current logged in user and their existing links to context data
        """
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        context["existing"] = self.model.objects.filter(
            user=self.request.user
        )
        context["title"] = self.title
        return context

    def get_success_url(self):
        """
        Redirect to the profile of the current logged in user upon successful operation
        """
        return reverse(
            "profile-detail",
            kwargs={"username": self.request.user.username},
        )

    def get_object(self):
        """
        Get link to update
        """
        return self.model.objects.get(
            pk=self.kwargs["pk"], user=self.request.user
        )


class LinkCreateView(LoginRequiredMixin, ManageLinksMixin, CreateView):
    """
    Add link to user profile
    Accessible by logged in users
    URL config: /link/create/
    """

    model = Link
    fields = ["url", "title"]
    template_name = "manage_links/link_form.html"
    title = "Add Link"


class LinkUpdateView(LoginRequiredMixin, ManageLinksMixin, UpdateView):
    """
    Update link
    Accessible by logged in users
    URL config: /link/<pk>/update/
    """

    model = Link
    fields = ["url", "title"]
    template_name = "manage_links/link_form.html"
    title = "Update Link"


class SocialMediaCreateView(
    LoginRequiredMixin, ManageLinksMixin, CreateView
):
    """
    Add social media button to user profile
    Accessible by logged in users
    URL config: /social/create/
    """

    model = SocialMedia
    fields = ["url", "name"]
    template_name = "manage_links/link_form.html"
    title = "Add Social Media"


class SocialMediaUpdateView(
    LoginRequiredMixin, ManageLinksMixin, UpdateView
):
    """
    Update social media button
    Accessible by logged in users
    URL config: /social/<pk>/update/
    """

    model = SocialMedia
    fields = ["url", "name"]
    template_name = "manage_links/link_form.html"
    title = "Update Social Media"


class LinkDeleteView(LoginRequiredMixin, ManageLinksMixin, DeleteView):
    """
    Delete link
    Accessible by logged in users
    URL config: /link/<pk>/delete/
    """

    model = Link
    template_name = "manage_links/link_form.html"

    def form_valid(self, form):
        # Reimplement original form_valid method
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class SocialMediaDeleteView(LinkDeleteView):
    """
    Delete social media button
    Accessible by logged in users
    URL config: /social/<pk>/delete/
    """

    model = SocialMedia
    template_name = "manage_links/link_form.html"
