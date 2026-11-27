from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tarea

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def configurar_nuevo_empleado(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        instance.is_staff = True
        instance.save(update_fields=['is_staff'])

        grupo, _ = Group.objects.get_or_create(name='Empleados')
        if not grupo.permissions.exists():
            content_type = ContentType.objects.get_for_model(Tarea)
            permisos = Permission.objects.filter(
                content_type=content_type,
                codename__in=['add_tarea', 'change_tarea', 'view_tarea']
            )
            grupo.permissions.set(permisos)

        instance.groups.add(grupo)
