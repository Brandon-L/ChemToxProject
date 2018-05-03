# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from home.models import experiment
from home.models import citation
from home.models import target
from home.models import chemicals
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
	return render(request, 'home/home.html')

def explore(request):
	experiment_table = experiment.objects.all()
	target_table = target.objects.all()
	citation_table = citation.objects.all()
	chemical_table = chemicals.objects.all()

	query = request.GET.get("q")
	tableview = request.GET.get("tableview", False)
	page = request.GET.get("page")

	if query:
		experiment_table = experiment.objects.filter(
			Q(aeid__icontains=query) |
			Q(assay_source_name__icontains=query) |
			Q(assay_source_long_name__icontains=query) |
			Q(assay_name__icontains=query) |
			Q(organism__icontains=query) |
			Q(tissue__icontains=query))


		target_table = target.objects.filter(
			Q(intended_target_official_full_name__icontains=query) |
			Q(intended_target_gene_name__icontains=query) |
			Q(intended_target_official_symbol__icontains=query) |
			Q(intended_target_gene_symbol__icontains=query) |
			Q(technological_target_official_full_name__icontains=query) |
			Q(technological_target_gene_name__icontains=query) |
			Q(technological_target_official_symbol__icontains=query) |
			Q(technological_target_gene_symbol__icontains=query))

		citation_table = citation.objects.filter(
			Q(pmid__icontains=query) |
			Q(doi__icontains=query) |
			Q(title__icontains=query) |
			Q(author__icontains=query))

		chemical_table = chemicals.objects.filter(
			Q(Substance_Name__icontains=query) |
			Q(Substance_CASRN__icontains=query) |
			Q(Structure_SMILES__icontains=query))

	exp_paginator = Paginator(experiment_table, 10)
	experiment_results = exp_paginator.get_page(page)
	tgt_paginator = Paginator(target_table, 10)
	target_results = tgt_paginator.get_page(page)
	cit_paginator = Paginator(citation_table, 10)
	citation_results = cit_paginator.get_page(page)
	chem_paginator = Paginator(chemical_table, 10)
	chemical_results = chem_paginator.get_page(page)

	args = {'experiment_results': experiment_results,
	'target_results': target_results, 'citation_results': citation_results,
	'chemical_results': chemical_results, 'tableview': tableview}
		
	return render(request, 'home/explore.html', args)

@login_required(login_url='/login/')
def manage(request):
	experiment_table = experiment.objects.all()
	target_table = target.objects.all()
	citation_table = citation.objects.all()
	chemical_table = chemicals.objects.all()

	tableview = request.GET.get("tableview", False)
	page = request.GET.get("page")
	delReq = request.GET.get("delete")

	exp_paginator = Paginator(experiment_table, 10)
	experiment_results = exp_paginator.get_page(page)
	tgt_paginator = Paginator(target_table, 10)
	target_results = tgt_paginator.get_page(page)
	cit_paginator = Paginator(citation_table, 10)
	citation_results = cit_paginator.get_page(page)
	chem_paginator = Paginator(chemical_table, 10)
	chemical_results = chem_paginator.get_page(page)


	args = {'experiment_results': experiment_results,
	'target_results': target_results, 'citation_results': citation_results,
	'chemical_results': chemical_results, 'tableview': tableview}

	return render(request, 'home/manage.html', args)
