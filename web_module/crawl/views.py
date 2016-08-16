from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.db.models.fields.files import FieldFile
from django.views.generic.base import TemplateView
from django.contrib import messages


# Create your views here.
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


class HomePageView(TemplateView):
    template_name = 'crawl/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'Hello http://example.com')
        return context



