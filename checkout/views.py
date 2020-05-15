from django.shortcuts import render, get_object_or_404


def donate(request):

    print(request.GET.get('game_project'))
    donation_type = request.GET.get('donation_type')
    game_project = request.GET.get('game_project')

    template = 'checkout/checkout.html'
    context = {
    }

    return render(request, template, context)
