from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.models import Cliente
from cars.repositories.cliente_repository import ClienteRepository
from cars.forms import ClienteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

cliente_repo = ClienteRepository()

# Vista para listar clientes
class ClienteListView(View):
    def get(self, request):
        clientes = cliente_repo.get_all()
        return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

# Vista para mostrar detalles de un cliente
class ClienteDetailView(View):
    def get(self, request, id):
        cliente = get_object_or_404(Cliente, id=id)
        return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

# Vista para eliminar un cliente
class ClienteDeleteView(View):
    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        cliente = get_object_or_404(Cliente, id=id)
        cliente.delete()
        messages.success(request, f'Cliente {cliente.user.username} eliminado con éxito.')
        return redirect('cliente_list')

# Vista para actualizar un cliente
class ClienteUpdateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request, id):
        cliente = get_object_or_404(Cliente, id=id)
        form = ClienteForm(instance=cliente)
        return render(request, 'clientes/cliente_update.html', {'form': form, 'cliente': cliente})

    @method_decorator(login_required(login_url='login'))
    def post(self, request, id):
        cliente = get_object_or_404(Cliente, id=id)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente {cliente.user.username} actualizado con éxito.')
            return redirect('cliente_list')
        return render(request, 'clientes/cliente_update.html', {'form': form, 'cliente': cliente})

# Vista para crear un nuevo cliente
class ClienteCreateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        # Filtrar solo los usuarios que tienen un perfil de cliente
        usuarios_disponibles = User.objects.filter(cliente__isnull=False)
        form = ClienteForm()
        form.fields['user'].queryset = usuarios_disponibles  # Limita el campo 'user' a usuarios sin cliente
        return render(request, 'clientes/cliente_create.html', {'form': form})

    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            if request.user.is_staff:  # Si el usuario actual que crea el cliente es staff
                cliente.is_staff_user = False  # Por defecto False para nuevos clientes
            cliente.save()  # Guarda el cliente en la base de datos
            messages.success(request, f'Cliente {cliente.user.username} creado con éxito.')
            return redirect('cliente_list')
        return render(request, 'clientes/cliente_create.html', {'form': form})
