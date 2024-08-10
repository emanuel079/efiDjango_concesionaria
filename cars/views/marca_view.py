from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.repositories.marca_repository import MarcaRepository
from cars.forms import MarcaForm

marca_repo = MarcaRepository()

class MarcaListView(View):
    def get(self, request):
        marcas = marca_repo.get_all()
        return render(request, 'marcas/list.html', {'marcas': marcas})

class MarcaDetailView(View):
    def get(self, request, id):
        marca = marca_repo.get_by_id(id)
        return render(request, 'marcas/detail.html', {'marca': marca})

class MarcaDeleteView(View):
    def get(self, request, id):
        marca = marca_repo.get_by_id(id)
        marca_repo.delete(marca)
        return redirect('marca_list')

class MarcaUpdateView(View):
    def get(self, request, id):
        marca = marca_repo.get_by_id(id)
        form = MarcaForm(instance=marca)
        return render(request, 'marcas/update.html', {'form': form})

    def post(self, request, id):
        marca = marca_repo.get_by_id(id)
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
        return render(request, 'marcas/update.html', {'form': form})

class MarcaCreateView(View):
    def get(self, request):
        form = MarcaForm()
        return render(request, 'marcas/create.html', {'form': form})

    def post(self, request):
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marca_list')
        return render(request, 'marcas/create.html', {'form': form})
