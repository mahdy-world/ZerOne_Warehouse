from datetime import datetime
from Core.models import SystemInformation
from Core.models import *


def allcontext(request):
    info = SystemInformation.objects.filter(id=1)
   

    modules = Modules.objects.all().last()
    today = datetime.now().date()
    context = { 
        'info':info,
        'modules':modules,
        'today':today,
    }
    return context