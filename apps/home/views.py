# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from home.forms import ec_relation_form
from home.models import citation
from home.models import experiment
from home.models import experiment_citation_relation
from home.models import experiment_target_relation

# Create your views here.
def homepage(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request, 'home/about.html')

def explore(request):
	ec_relation = experiment_citation_relation.objects.all()
	et_relation = experiment_target_relation.objects.all()

	query = request.GET.get("q")
	if query:
		ec_relation = experiment_citation_relation.objects.filter(aeid__assay_source_name__icontains=query)
		et_relation = experiment_target_relation.objects.filter(aeid__assay_source_name__icontains=query)

	args = {'ec_relation':ec_relation, 'et_relation': et_relation}
		
	return render(request, 'home/explore.html', args)

def manage(request):
	ec_relation = experiment_citation_relation.objects.all()
	et_relation = experiment_target_relation.objects.all()

	form = ec_relation_form()
	
	if request.method == "POST":
		exp_model = experiment.objects.get(aeid = request.POST.get("aeid") )
		citation_model = citation.objects.get(citation_id = request.POST.get("citation_id"))
		experiment_citation_relation.objects.create(aeid=exp_model, citation_id=citation_model)

	args = {'ec_relation':ec_relation, 'et_relation': et_relation, 'form':form}

	return render(request, 'home/manage.html', args)
