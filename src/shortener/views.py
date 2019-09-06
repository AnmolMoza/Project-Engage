from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import SubmitUrlForm
from .models import ShorURL
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
		if form.is_valid():
			print(form.cleaned_data.get('url'))
		context = {
			"title":"ShorURL ",
			"form": form
		}
		return render(request, "shortener/home.html", context)

class ShorCBView(View):
	def get(self, request, shortcode= None, *args, **kwargs): #Class Based Views
		obj = get_object_or_404(ShorURL, shortcode = shortcode) #Handles POST and GIT by function, is portable but takes more lines of code
		return HttpResponseRedirect(obj.url)