# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from cars.models import Comentario, Auto
from cars.forms import ComentarioForm
import logging
from users.models import Profile
from django.utils.translation import (
    activate,
    get_language,
    gettext_lazy as _,
    deactivate
)

# Configura el logger para capturar mensajes de depuración y errores
logger = logging.getLogger(__name__)

# Vista para listar comentarios de un auto específico
class ComentariosPorAutoView(View):
    def get(self, request, auto_pk, *args, **kwargs):
        if not request.user.is_anonymous:
            profile = Profile.objects.get(user=request.user)
            lang = profile.language
            activate(lang)
        auto = get_object_or_404(Auto, pk=auto_pk)
        comentarios = Comentario.objects.filter(auto=auto)
        return render(
            request,
            'comentarios/list.html',
            {'comentarios': comentarios, 'auto': auto}
        )

# Vista para crear un nuevo comentario asociado a un auto
@method_decorator(login_required(login_url='login'), name='dispatch')
class ComentarioCreateView(View):
    def get(self, request, auto_pk):
        auto = get_object_or_404(Auto, pk=auto_pk)
        form = ComentarioForm()
        return render(
            request,
            'comentarios/create.html',
            {'form': form, 'auto': auto}
        )

    def post(self, request, auto_pk):
        auto = get_object_or_404(Auto, pk=auto_pk)

        # Obtiene el usuario desde el request
        user = request.user

        # Verifica si el usuario es un cliente
        if not user.is_staff:  # Aquí verificamos si no es staff
            logger.debug(f"Usuario registrado: {user}")
        else:
            # Log de error y mensaje para usuario si no es cliente
            logger.error("El usuario no es un cliente registrado")
            messages.error(request, "Debes ser un cliente registrado para comentar.")
            return redirect('comentarios_por_auto', auto_pk=auto.pk)

        # Procesa el formulario
        form = ComentarioForm(request.POST)
        if form.is_valid():
            logger.debug("Formulario es válido")
            comentario = form.save(commit=False)
            comentario.usuario = user  # Asigna el usuario
            comentario.auto = auto
            try:
                comentario.save()  # Guarda el comentario en la base de datos
                logger.debug("Comentario guardado con éxito")
                messages.success(request, "Comentario agregado con éxito.")
            except Exception as e:
                # Captura excepciones en el guardado
                logger.error("Error al guardar el comentario")
                logger.error(str(e))
                messages.error(request, "Hubo un error al guardar el comentario.")
            return redirect('comentarios_por_auto', auto_pk=auto.pk)
        else:
            # Log de errores del formulario
            logger.error("Formulario no es válido")
            logger.error(form.errors)  # Imprime errores del formulario
        
        return render(
            request,
            'comentarios/create.html',
            {'form': form, 'auto': auto}
        )

# Vista para mostrar el detalle de un comentario
class ComentarioDetailView(View):
    def get(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        return render(
            request,
            'comentarios/detail.html',
            {'comentario': comentario}
        )

# Vista para actualizar un comentario
class ComentarioUpdateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        form = ComentarioForm(instance=comentario)
        return render(
            request,
            'comentarios/update.html',
            {'form': form}
        )

    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            # Actualiza el comentario con los datos del formulario
            comentario.comentario = form.cleaned_data['comentario']
            comentario.save()
            messages.success(request, "Comentario actualizado con éxito.")
            return redirect('comentarios_por_auto', auto_pk=comentario.auto.pk)
        else:
            # Log de errores del formulario
            logger.error("Formulario no es válido")
            logger.error(form.errors)
        
        return render(
            request,
            'comentarios/update.html',
            {'form': form}
        )

# Vista para eliminar un comentario
class ComentarioDeleteView(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request, pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        auto_pk = comentario.auto.pk
        comentario.delete()
        messages.success(request, "Comentario eliminado con éxito.")
        return redirect('comentarios_por_auto', auto_pk=auto_pk)
