from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from webapp.models.labores import Labores

def labor(request):
    numerolabores=Labores.objects.count()
    labores=Labores.objects.order_by('id')
    return render(request, 'labores.html', {'no_labores': numerolabores, 'Labor': labores})
