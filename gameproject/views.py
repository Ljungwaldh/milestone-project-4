from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import GameProject
from subscription.models import Donation
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.contrib import messages
from .forms import ProjectForm


def all_projects(request):

    game_projects = GameProject.objects.all()
    profile = get_object_or_404(Profile, user=request.user)

    template = 'gameproject/all_projects.html'
    context = {
        'game_projects': game_projects,
        'profile': profile
    }

    return render(request, template, context)


def project_detail(request, project_id):

    game_project = get_object_or_404(GameProject, pk=project_id)
    donation_options = Donation.objects.all()

    template = 'gameproject/project_detail.html'
    context = {
        'game_project': game_project,
        'donation_options': donation_options
    }

    return render(request, template, context)


@login_required
def add_project(request):

    profile = get_object_or_404(Profile, user=request.user)

    if not profile.is_creator:
        messages.error(request, 'Sorry, only creators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Successfully created project!')
            return redirect(reverse('project_detail', args=[project.id]))
        else:
            messages.error(request, 'Failed to create project. Please ensure the form is valid')

    project_form = ProjectForm()

    template = 'gameproject/add_project.html'
    context = {
        'project_form': project_form,
    }

    return render(request, template, context)


@login_required
def edit_project(request, project_id):

    profile = get_object_or_404(Profile, user=request.user)
    project = get_object_or_404(GameProject, pk=project_id)

    if not profile.is_creator:
        messages.error(request, 'Sorry, only creators can do that.')
        return redirect(reverse('home'))
    elif not project.owner:
        messages.error(request, 'Sorry, only the project owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, instance=project)
        if project_form.is_valid():
            project_form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Successfully updated project!')
            return redirect(reverse('project_detail', args=[project.id]))
        else:
            messages.error(request, 'Failed to update project. Please ensure the form is valid.')
    else:
        project_form = ProjectForm(instance=project)
        messages.info(request, f'You are editing {project.title}')

    template = 'gameproject/edit_project.html'
    context = {
        'project_form': project_form,
        'project': project,
    }

    return render(request, template, context)
