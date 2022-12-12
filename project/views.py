from django.shortcuts import render, redirect
from .models import Project, Review
from .forms import ProjectForm, ReviewForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.



def project(request, pk):
	# project instance requested
	project = Project.objects.get(id = pk)
	# context
	context = {'project': project}
	# path to template
	template = 'project/single-project.html'

	return render(request, template, context)

def projects(request):
	# path to template
	template = 'project/projects.html'
	# Project instances
	projects = Project.objects.all()
	# context
	context = {'projects': projects}

	return render(request, template, context)

@staff_member_required
def createProject(request):
	# path to template
	template = 'project/project-form.html'
	# instance 
	form = ProjectForm()

	# if post
	if request.method == 'POST':
		# fill in the form
		form = ProjectForm(request.POST, request.FILES)
		# check validity
		if form.is_valid():
			# save
			form.save()
			# redirect to projects url
			return redirect('project:projects')

	# context
	context = {'form': form}

	return render(request, template, context)

@staff_member_required
def updateProject(request, pk):
	# path to template
	template = 'project/project-form.html'
	# project instance requested
	project = Project.objects.get(id = pk)
	# form
	form = ProjectForm(instance = project)

	if request.method == 'POST':
		# fill in the form
		form = ProjectForm(request.POST, request.FILES, instance = project)
		# check validity
		if form.is_valid():
			# save
			form.save()
			# redirect to projects url
			return redirect('project:projects') 

	# context
	context = {'form': form}

	return render(request, template, context)

@staff_member_required
def deleteProject(request, pk):
	# path to template
	template = 'project/delete-project.html'
	# project instance requested
	project = Project.objects.get(id = pk)

	if request.method == 'POST':
		project.delete()
		return redirect('project:projects')

	# context
	context = {'project': project}

	return render(request, template, context)

@staff_member_required
def createReview(request, pk):
	# path to template
	template = 'project/review-form.html'
	# project instance requested
	form = ReviewForm()

	if request.method == 'POST':
		# fill in the form
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('project:project', pk = pk)

	# context
	context = {'form': form}

	return render(request, template, context)

		# def createReview(request, pk):
		# 	# path to template
		# 	template = 'project/delete-project'
		# 	# project instance requested
		# 	project = Project.objects.get(id = pk)

		# 	if request.Method == 'POST':
		# 		project.delete()
		# 		return redirect('projects')

		# 	# context
		# 	context = {'project': project}

		# 	return render(request, template, context)