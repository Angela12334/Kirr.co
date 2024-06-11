import string
import random
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from analytics.models import ClickEvent
from.models import KirrURL
from.forms import SubmitUrlForm
import pyperclip
# Create your views here.

def copy_link(request, shortcode=None):
    pyperclip.copy(shortcode)
    the_form= SubmitUrlForm()
    context = {
            "title": "Kirr.co",
            "form": the_form
        }
    return render(request, "shortener/home.html", context)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form= SubmitUrlForm()
        context = {
            "title": "Kirr.co",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
                "title":"Kirr.co",
                "form": form}
        template = "shortener/home.html"
        if form.is_valid():
            shortcode = ''.join(random.choice(string.ascii_letters) for x in range(10))
            new_url = form.cleaned_data.get("url")
            obj = KirrURL.objects.filter(url=new_url)
            if obj.exists():
                obj = obj[0]
                template = "shortener/already-exists.html"
                context = {
                "object": obj,
                "created": False,
                }
            else:
                obj, created = KirrURL.objects.get_or_create(url=new_url, shortcode=shortcode)
                template = "shortener/success.html"
                context = {
                    "object": obj,
                    "created": created,
                }
        return render(request, template, context)

class URLRedirectView(View):
    def get(self, request, shortcode=None,  *args, **kwargs):
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponse(obj.url)








