from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .utils import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.duration),
            'is_strange': visit.is_long(),
        }
        for visit in Visit.objects.filter(passcard=passcard)
    ]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
