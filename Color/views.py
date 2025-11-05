from django.views import View 
from django.shortcuts import render
from .forms import ThingForm, ThingModelForm
from .models import Thing, Color

class Home(View):
	def get(self, request):
		return render(request,'home.html',{"form":ThingModelForm})
	def post(self, request):
		f = ThingModelForm(request.POST)
		list = Thing.objects.all().values()
		if f.is_valid():
			f.save()
			f = ThingModelForm()
		return render(request, 'home.html',{"form":f,"list":list})
