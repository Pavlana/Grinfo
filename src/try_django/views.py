from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
	title = "Hello, Grinfos!"
	template = 'home.html'
	if request.user.is_authenticated:
		user = request.user
	context = {"title": title}
	return render(request, template, context)


def about_page(request):
	return render(request, 'about.html', {"title": 'About'})


def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
		'title': 'Contact us',
		'form' : form
	}
	return render(request, 'form.html', context)