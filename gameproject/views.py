from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import GameProject, Donation
from checkout.models import Order
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.contrib import messages
from .forms import ProjectForm
from django.db.models import Q


@login_required
def all_projects(request):

    game_projects = GameProject.objects.all()
    profile = get_object_or_404(Profile, user=request.user)
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('all_projects'))

        queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(owner__user__username__icontains=query)
        game_projects = game_projects.filter(queries)

    for game_project in game_projects:
        game_project.total_amount = 0
        for order in Order.objects.filter(game_project=game_project).filter(status='PA'):
            game_project.total_amount += order.donation_item.amount

    template = 'gameproject/all_projects.html'
    context = {
        'game_projects': game_projects,
        'profile': profile,
        'search_term': query
    }

    return render(request, template, context)


@login_required
def project_detail(request, project_id):

    game_project = get_object_or_404(GameProject, pk=project_id)
    donation_options = Donation.objects.all()
    profile = get_object_or_404(Profile, user=request.user)

    game_project.total_amount = 0
    for order in Order.objects.filter(game_project=game_project).filter(status='PA'):
        game_project.total_amount += order.donation_item.amount

    template = 'gameproject/project_detail.html'
    context = {
        'game_project': game_project,
        'donation_options': donation_options,
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def add_project(request):

    profile = get_object_or_404(Profile, user=request.user)

    if not profile.is_creator:
        messages.error(request, 'Sorry, only creators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Successfully created project!')
            return redirect(reverse('project_detail', args=[project.id]))
        else:
            messages.error(
                request,
                'Failed to create project. Please ensure the form is valid'
                )

    project_form = ProjectForm()

    template = 'gameproject/add_project.html'
    context = {
        'project_form': project_form,
    }

    return render(request, template, context)


@login_required
def edit_project(request, game_project_id):

    profile = get_object_or_404(Profile, user=request.user)
    game_project = get_object_or_404(GameProject, pk=game_project_id)

    if not profile.is_creator:
        messages.error(request, 'Sorry, only creators can do that.')
        return redirect(reverse('home'))
    if game_project.owner != profile:
        messages.error(request, 'Sorry, only the project owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        game_project_form = ProjectForm(
            request.POST,
            request.FILES,
            instance=game_project
            )
        if game_project_form.is_valid():
            game_project_form.save(commit=False)
            game_project.owner = profile
            game_project.total_amount = 0
            for order in Order.objects.filter(game_project=game_project).filter(status='PA'):
                game_project.total_amount += order.donation_item.amount
            game_project.save()
            messages.success(request, 'Successfully updated project!')
            return redirect(reverse('project_detail', args=[game_project.id]))
        else:
            messages.error(
                request,
                'Failed to update project. Please ensure the form is valid.'
                )
    else:
        game_project_form = ProjectForm(instance=game_project)
        messages.info(request, f'You are editing {game_project.title}')

    template = 'gameproject/edit_project.html'
    context = {
        'game_project_form': game_project_form,
        'game_project': game_project,
    }

    return render(request, template, context)


@login_required
def delete_project(request, project_id):

    profile = get_object_or_404(Profile, user=request.user)
    project = get_object_or_404(GameProject, pk=project_id)

    if not profile.is_creator:
        messages.error(request, 'Sorry, only creators can do that.')
        return redirect(reverse('home'))
    if project.owner != profile:
        messages.error(request, 'Sorry, only the project owner can do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(GameProject, pk=project_id)
    project.delete()
    messages.success(request, 'Project deleted!')
    return redirect(reverse('all_projects'))
