from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from cars.repositories.cita_repository import CitaRepository
from cars.forms import CitaForm
from cars.models import Cita, Cliente

cita_repo = CitaRepository()

# Vista para mostrar los detalles de una cita
class CitaDetailView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        cita = get_object_or_404(Cita, id=id)
        
        # Verificar si el usuario puede ver esta cita
        if not request.user.is_staff and cita.cliente.user != request.user:
            messages.error(request, 'No tienes permiso para ver esta cita.')
            return redirect('cita_list')

        return render(request, 'cita/cita_detail.html', {'cita': cita})

# Vista para eliminar una cita
@method_decorator(login_required, name='dispatch')
class CitaDeleteView(View):
    def get(self, request, id):
        cita = get_object_or_404(Cita, id=id)
        return render(request, 'cita/cita_delete.html', {'cita': cita})

    def post(self, request, id):
        cita = get_object_or_404(Cita, id=id)
        cita.delete()
        messages.success(request, 'Cita eliminada con éxito.')
        return redirect('cita_list')

# Vista para actualizar una cita
class CitaUpdateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        cita = get_object_or_404(Cita, id=id)
        form = CitaForm(instance=cita)
        return render(request, 'cita/cita_update.html', {'form': form, 'cita': cita})

    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        cita = get_object_or_404(Cita, id=id)
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita actualizada con éxito.')
            return redirect('cita_detail', id=cita.id)
        return render(request, 'cita/cita_update.html', {'form': form, 'cita': cita})


# Vista para listar todas las citas
class CitaListView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        if request.user.is_staff:
            # Obtener todas las citas para los usuarios staff
            citas = cita_repo.get_all()
        else:
            # Obtener citas solo para el cliente logueado
            cliente = get_object_or_404(Cliente, user=request.user)
            citas = cita_repo.get_by_cliente(cliente)

        return render(request, 'cita/cita_list.html', {'citas': citas})
# Vista para crear una nueva cita
class CitaCreateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        if request.user.is_staff:
            messages.error(request, 'Los usuarios `staff` no pueden crear citas.')
            return redirect('cita_list')

        form = CitaForm()
        form.fields['cliente'].queryset = Cliente.objects.filter(user=request.user)
        return render(request, 'cita/cita_create.html', {'form': form})

    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        if request.user.is_staff:
            messages.error(request, 'Los usuarios `staff` no pueden crear citas.')
            return redirect('cita_list')

        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cliente = get_object_or_404(Cliente, user=request.user)
            cita.cliente = cliente  # Asegúrate de asignar la instancia de cliente
            cita.save()
            messages.success(request, 'Cita creada con éxito.')
            return redirect('cita_list')

        return render(request, 'cita/cita_create.html', {'form': form})