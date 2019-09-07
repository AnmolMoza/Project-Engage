from django import forms

from .validators import validate_url

class SubmitUrlForm(forms.Form):
	url = forms.CharField(
		label = '', 
		validators = [validate_url],
		widget = forms.TextInput(
				attrs = {
					"placeholder": "Long URL",
					"class": "form-control"
					}
			)
		)

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

	#def clean_url(self):
	#	url = self.cleaned_data['url']
	#	if "http" in url:
	#		return url
	#	return "http://" + url