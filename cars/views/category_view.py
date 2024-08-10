from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.repositories.category_repository import CategoriaRepository
from cars.forms import CategoriaForm

categoria_repo = CategoriaRepository()

class CategoriaListView(View):
    def get(self, request):
        categorias = categoria_repo.get_all()
        return render(request, 'categorias/list.html', {'categorias': categorias})

class CategoriaDetailView(View):
    def get(self, request, id):
        categoria = categoria_repo.get_by_id(id)
        return render(request, 'categorias/detail.html', {'categoria': categoria})

class CategoriaDeleteView(View):
    def get(self, request, id):
        categoria = categoria_repo.get_by_id(id)
        categoria_repo.delete(categoria)
        return redirect('categoria_list')

class CategoriaUpdateView(View):
    def get(self, request, id):
        categoria = categoria_repo.get_by_id(id)
        form = CategoriaForm(instance=categoria)
        return render(request, 'categorias/update.html', {'form': form})

    def post(self, request, id):
        categoria = categoria_repo.get_by_id(id)
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
        return render(request, 'categorias/update.html', {'form': form})

class CategoriaCreateView(View):
    def get(self, request):
        form = CategoriaForm()
        return render(request, 'categorias/create.html', {'form': form})

    def post(self, request):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
        return render(request, 'categorias/create.html', {'form': form})
