from django import forms
from home.models import experiment

class experiment_form(forms.ModelForm):
	class Meta:
		model = experiment
		fields = [
			"assay_source_name",
			"assay_source_long_name",
			"assay_name",
			"organism",
			"tissue"
		]

