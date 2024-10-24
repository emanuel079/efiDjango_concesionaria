from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.repositories.servicio_repository import ServicioRepository
from cars.forms import ServicioForm

servicio_repo = ServicioRepository()

class ServicioListView(View):
    def get(self, request):
        servicios = servicio_repo.get_all()
        return render(request, 'servicios/list.html', {'servicios': servicios})

class ServicioDetailView(View):
    def get(self, request, id):
        servicio = servicio_repo.get_by_id(id)
        return render(request, 'servicios/detail.html', {'servicio': servicio})

class ServicioDeleteView(View):
    def get(self, request, id):
        servicio = servicio_repo.get_by_id(id)
        servicio_repo.delete(servicio)
        return redirect('servicio_list')

class ServicioUpdateView(View):
    def get(self, request, id):
        servicio = servicio_repo.get_by_id(id)
        form = ServicioForm(instance=servicio)
        return render(request, 'servicios/update.html', {'form': form})

    def post(self, request, id):
        servicio = servicio_repo.get_by_id(id)
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('servicio_list')
        return render(request, 'servicios/update.html', {'form': form})

class ServicioCreateView(View):
    def get(self, request):
        form = ServicioForm()
        return render(request, 'servicios/create.html', {'form': form})

    def post(self, request):
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicio_list')
        return render(request, 'servicios/create.html', {'form': form})
