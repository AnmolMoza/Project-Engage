from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ShorURL
# Create your views here.


class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "shortener/home.html", {})


class ShorCBView(View):
	def get(self, request, shortcode= None, *args, **kwargs): #Class Based Views
		obj = get_object_or_404(ShorURL, shortcode = shortcode) #Handles POST and GIT by function, is portable but takes more lines of code
		return HttpResponseRedirect(obj.url)