from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.repositories.modelo_auto_repository import ModeloAutoRepository
from cars.forms import ModeloAutoForm

modelo_auto_repo = ModeloAutoRepository()

class ModeloAutoListView(View):
    def get(self, request):
        modelos = modelo_auto_repo.get_all()
        return render(request, 'modelos/list.html', {'modelos': modelos})

class ModeloAutoDetailView(View):
    def get(self, request, id):
        modelo = modelo_auto_repo.get_by_id(id)
        return render(request, 'modelos/detail.html', {'modelo': modelo})

class ModeloAutoDeleteView(View):
    def get(self, request, id):
        modelo = modelo_auto_repo.get_by_id(id)
        modelo_auto_repo.delete(modelo)
        return redirect('modelo_auto_list')

class ModeloAutoUpdateView(View):
    def get(self, request, id):
        modelo = modelo_auto_repo.get_by_id(id)
        form = ModeloAutoForm(instance=modelo)
        return render(request, 'modelos/update.html', {'form': form})

    def post(self, request, id):
        modelo = modelo_auto_repo.get_by_id(id)
        form = ModeloAutoForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('modelo_auto_list')
        return render(request, 'modelos/update.html', {'form': form})

class ModeloAutoCreateView(View):
    def get(self, request):
        form = ModeloAutoForm()
        return render(request, 'modelos/create.html', {'form': form})

    def post(self, request):
        form = ModeloAutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modelo_auto_list')
        return render(request, 'modelos/create.html', {'form': form})
