from django import forms

from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
	url = forms.CharField(label = 'Submit URL', validators = [validate_url, validate_dot_com])

	#def clear(self): #Form validation, cleaning a specif field attribute 
	#	cleaned_data = super(SubmitUrlForm, self).clean() #validating direcctly the form
	#	print(cleaned_data)
	#	url = cleaned_data("url") #doing for above form
	#	url_validator  = URLValidator()
	#	try:
	#		url_validator(url)
	#	except:
	#		raise forms.ValidationError("Invalid URL for this field")
	#	return url
		#print(url)

	#def clean_url(self): #second way, validation te form
	#	url = self.cleaned_data['url']
	#	print(url)
	#	url_validator  = URLValidator()
	#	try:
	#		url_validator(url)
	#	except:
	#		raise forms.ValidationError("Invalid URL for this field")
	#	return url