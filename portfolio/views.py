from django.shortcuts import render
from django.contrib.auth.mixins import (
	LoginRequiredMixin, 
	UserPassesTestMixin
)
from django.views.generic import ( 
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Project


def home(request):
	context = {
		'projects': Project.objects.all()
	}
	return render(request, 'portfolio/home.html', context)

class ProjectListView(ListView):
	model = Project
	template_name = 'portfolio/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'projects'
	ordering = ['-date_completed']

class ProjectDetailView(DetailView):
	model = Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
	model = Project
	fields = ['name', 'language', 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Project
	fields = ['name', 'language', 'description']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		project = self.get_object()
		if self.request.user == project.author:
			return True
		return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Project
	success_url = '/'

	def test_func(self):
		project = self.get_object()
		if self.request.user == project.author:
			return True
		return False

def about(request):
	return render(request, 'portfolio/about.html', {'title': 'About'})