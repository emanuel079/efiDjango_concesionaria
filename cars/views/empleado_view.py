from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.models import Empleado

from cars.repositories.empleado_respository import EmpleadoRepository
from cars.forms import EmpleadoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

empleado_repo = EmpleadoRepository()

# Vista para listar empleados
class EmpleadoListView(View):
    def get(self, request):
        empleados = empleado_repo.get_all()
        return render(request, 'empleados/empleados_list.html', {'empleados': empleados})

# Vista para detalles de un empleado
class EmpleadoDetailView(View):
    def get(self, request, id):
        empleado = empleado_repo.get_by_id(id)
        return render(request, 'empleados/empleados_detail.html', {'empleado': empleado})

# Vista para eliminar un empleado
class EmpleadoDeleteView(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        # Asegúrate de obtener correctamente el empleado usando get_object_or_404
        empleado = get_object_or_404(Empleado, id=id)  # Cambiar 'empleado' por 'Empleado' con mayúscula

        # Eliminar el empleado
        empleado.delete()

        # Enviar un mensaje de éxito
        messages.success(request, f'Empleado {empleado.user.username} eliminado con éxito.')

        # Redirigir a la lista de empleados
        return redirect('empleados_list')

        

# Vista para actualizar un empleado
class EmpleadoUpdateView(View):
    def get(self, request, id):
        empleado = empleado_repo.get_by_id(id)
        form = EmpleadoForm(instance=empleado)
        return render(request, 'empleados/empleados_update.html', {'form': form, 'empleado': empleado})

    def post(self, request, id):
        empleado = empleado_repo.get_by_id(id)
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, f'Empleado {empleado.user.username} actualizado con éxito.')
            return redirect('empleados_list')
        return render(request, 'empleados/empleados_update.html', {'form': form, 'empleados': empleado})

# Vista para crear un nuevo empleado
class EmpleadoCreateView(View):
    def get(self, request):
        form = EmpleadoForm()
        return render(request, 'empleados/empleados_create.html', {'form': form})

    def post(self, request):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.user.is_staff = True  # Marca al usuario como staff
            empleado.user.save()
            empleado.save()
            messages.success(request, f'Empleado {empleado.user.username} creado con éxito.')
            return redirect('empleados_list')
        return render(request, 'empleados/empleados_create.html', {'form': form})
