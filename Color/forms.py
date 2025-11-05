from .models import Color, Thing
from django import forms 

class ThingForm(forms.Form):
	name = forms.CharField(label="Name of thing: ",max_length=20)
	color = forms.ModelChoiceField(Color.objects.all())

class ThingModelForm(forms.ModelForm):
		class Meta:
				model = Thing
				fields = ['name', 'color']