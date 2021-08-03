from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .utils import format_duration


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.duration),
        }
        for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
