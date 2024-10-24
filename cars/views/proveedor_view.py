from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.repositories.proveedor_repository import ProveedorRepository
from cars.forms import ProveedorForm

proveedor_repo = ProveedorRepository()

class ProveedorListView(View):
    def get(self, request):
        proveedores = proveedor_repo.get_all()
        return render(request, 'proveedores/proveedores_list.html', {'proveedores': proveedores})

class ProveedorDetailView(View):
    def get(self, request, pk):  
        proveedor = proveedor_repo.get_by_id(pk)
        return render(request, 'proveedores/proveedores_detail.html', {'proveedor': proveedor})

class ProveedorDeleteView(View):
    def get(self, request, pk):  
        proveedor = proveedor_repo.get_by_id(pk)
        proveedor_repo.delete(proveedor)
        return redirect('proveedores_list') 

class ProveedorUpdateView(View):
    def get(self, request, pk):  
        proveedor = proveedor_repo.get_by_id(pk)
        form = ProveedorForm(instance=proveedor)
        return render(request, 'proveedores/proveedores_update.html', {'form': form})

    def post(self, request, pk):  
        proveedor = proveedor_repo.get_by_id(pk)
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores_list')  
        return render(request, 'proveedores/proveedores_update.html', {'form': form})

class ProveedorCreateView(View):
    def get(self, request):
        form = ProveedorForm()
        return render(request, 'proveedores/proveedores_create.html', {'form': form})

    def post(self, request):
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores_list')  
        return render(request, 'proveedores/proveedores_create.html', {'form': form})