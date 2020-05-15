from django.shortcuts import render, get_object_or_404
from .models import GameProject
from subscription.models import Donation




def all_projects(request):

    game_projects = GameProject.objects.all()

    template = 'gameproject/all_projects.html'
    context = {
        'game_projects': game_projects
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
