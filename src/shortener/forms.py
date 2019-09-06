from django import forms

from django.core.validators import ValidationError
from django.core.validators import URLValidator

def validate_url(value): #Custom Validator 
	url_validator = URLValidator
	try:
		url_validator(value)
	except:
		raise ValidationError("Invalid URL for this field")
	return value

def validate_dot_com(value):
	if not "com" in value:
		raise ValidationError("This is not valid because of no .com")
	return value
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