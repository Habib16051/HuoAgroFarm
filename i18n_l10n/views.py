from django.shortcuts import render
from django.utils.translation import gettext as _


def Local_Language(request):
    greeting = _("Hello, world!")
    return render(request, 'multiL/translator.html', {'greeting': greeting})
# Create your views here.
