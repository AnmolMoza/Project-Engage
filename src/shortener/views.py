from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from .forms import SubmitUrlForm
from .models import ShorURL
from analytics.models import ClickEvent
# Create your views here.

def home_view_fbv(request,*args, **kwargs):
	if request.methord == "POST":
		print(request.POST)
	return render(request, "shortener/home.html", {})


class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title":"ShorURL ",
			"form": the_form
		}
		return render(request, "shortener/home.html", context)

	def post(self,request,*args,**kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title":"ShorURL.co",
			"form": form
		}
		template = "shortener/home.html" #makes page dynamic, pages change but url doesn't
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = ShorURL.objects.get_or_create(url=new_url)
			context = {
			"object": obj,
			"created": created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-created.html"
		return render(request, template, context)

class URLRedirectView(View):
	def get(self, request, shortcode= None, *args, **kwargs): #Class Based Views
		qs = ShorURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
		