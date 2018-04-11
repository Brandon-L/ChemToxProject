from django import forms
from home.models import experiment_citation_relation

class ec_relation_form(forms.ModelForm):
	class Meta:
		model = experiment_citation_relation
		fields = [
			"aeid",
			"citation_id"
		]