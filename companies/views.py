from django.db.models.base import Model
from django.shortcuts import render, redirect, get_object_or_404
from .models import Companies
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View
from django.db.models import Q

from django.contrib import messages
from django.views.generic import (
	TemplateView,
	ListView,
	CreateView,
	DetailView,
	UpdateView,
	DeleteView,
	)


# Create your views here.


class CompanyListView(View):
	template_name = 'companyList.html'
	queryset_list = Companies.objects.all()

	def get(self, request, *args, **kwargs):
		queryset_list = Companies.objects.all()
		query = request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(description__icontains=query)|
				Q(founder__icontains=query)
				).distinct()
		
		def get_queryset(self):
			return self.queryset_list


		context  = {'company': queryset_list, 'query': query}
		return render(request, self.template_name, context)





class CompanyCreateView(LoginRequiredMixin, CreateView):
	model = Companies
	template_name = 'companyCreate.html'
	fields = [
		'name',
		'logo',
		'founder',
		'company_type',
		'whenfounded',
		'description',
	]
	# messages.success(request, f'Company has been successfully added')

	def form_valid(self, form):
		return super().form_valid(form)


class CompanyDetailView(DetailView):
	template_name = 'company_detail.html'
	model = Companies
	context_object_name = 'comp'


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'update_company.html'
	fields = ['name', 'founder', 'description', 'whenfounded']
	model = Companies

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'companies_confirm_delete.html'
	model = Companies
	success_url = '/companies/'