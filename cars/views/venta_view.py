from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.repositories.venta_repository import VentaRepository
from cars.forms import VentaForm

venta_repo = VentaRepository()

class VentaListView(View):
    def get(self, request):
        ventas = venta_repo.get_all()
        return render(request, 'ventas/list.html', {'ventas': ventas})

class VentaDetailView(View):
    def get(self, request, id):
        venta = venta_repo.get_by_id(id)
        return render(request, 'ventas/detail.html', {'venta': venta})

class VentaDeleteView(View):
    def get(self, request, id):
        venta = venta_repo.get_by_id(id)
        venta_repo.delete(venta)
        return redirect('venta_list')

class VentaUpdateView(View):
    def get(self, request, id):
        venta = venta_repo.get_by_id(id)
        form = VentaForm(instance=venta)
        return render(request, 'ventas/update.html', {'form': form})

    def post(self, request, id):
        venta = venta_repo.get_by_id(id)
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
        return render(request, 'ventas/update.html', {'form': form})

class VentaCreateView(View):
    def get(self, request):
        form = VentaForm()
        return render(request, 'ventas/create.html', {'form': form})

    def post(self, request):
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
        return render(request, 'ventas/create.html', {'form': form})
