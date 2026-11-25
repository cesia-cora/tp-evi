from django.http import JsonResponse
from django.db.models import Count
from .models import Tarea

def reporte_tareas(request):
    total = Tarea.objects.count()
    por_estado = list(Tarea.objects.values('estado').annotate(cantidad=Count('estado')))
    return JsonResponse({
        'total_tareas': total,
        'resumen_por_estado': por_estado
    })
