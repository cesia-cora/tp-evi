from django.contrib import admin
from django.http import HttpResponse
from .models import Tarea
import csv

@admin.action(description="Exportar tareas seleccionadas a CSV")
def exportar_tareas_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = 'attachment; filename="todo_list.csv"'
    response.write("\ufeff")

    writer = csv.writer(response)
    writer.writerow(["ID", "Título", "Completada", "Creada"])

    for tarea in queryset:
        writer.writerow([
            tarea.id,
            tarea.titulo,
            "Sí" if tarea.completada else "No",
            tarea.creada_en.strftime("%Y-%m-%d %H:%M") if getattr(tarea, "creada_en", None) else "",
        ])

    return response

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empleado', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'empleado')
    search_fields = ('titulo', 'empleado')
    actions = [exportar_tareas_csv]