from django.shortcuts import render
from .models import Project

projects = [
	{
	'name': 'Subreddit Keyword Search',
	'language': "Python",
	'description': 'Created an application that searches r/ProgrammerHumor using any keyword and populates an excel file in order of the score',
	'date_completed': 'October 14, 2020',
	},
	{
	'name': 'Website portfolio',
	'language': "Python, Django",
	'description': 'Created this website using Django and programmed the server using Linode',
	'date_completed': 'January 11, 2020',
	},
	

]

def home(request):
	context = {
		'projects': Project.objects.all()
	}
	return render(request, 'portfolio/home.html', context)

def about(request):
	return render(request, 'portfolio/about.html', {'title': 'About'})