from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from manage_links.models import Link, SocialMedia

# Add link to user profile
class AddLinkView(CreateView):
    model = Link
    fields = ['url', 'title']
