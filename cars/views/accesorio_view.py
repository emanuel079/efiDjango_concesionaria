from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cars.repositories.accesorio_repository import AccesorioRepository
from cars.forms import AccesorioForm

# Vista basada en clase para listar todos los accesorios
class AccesorioListView(View):
    def get(self, request):
        accesorio_repository = AccesorioRepository()
        accesorios = accesorio_repository.get_all()
        return render(request, 'accesorios/accesorios_list.html', {'accesorios': accesorios})

# Vista basada en clase para mostrar el detalle de un accesorio
class AccesorioDetailView(View):
    def get(self, request, pk):
        accesorio_repository = AccesorioRepository()
        accesorio = accesorio_repository.get_by_id(pk)
        return render(request, 'accesorios/accesorios_detail.html', {'accesorio': accesorio})

# Vista basada en clase para eliminar un accesorio
class AccesorioDeleteView(View):
    def get(self, request, pk):
        accesorio_repository = AccesorioRepository()
        accesorio = accesorio_repository.get_by_id(pk)
        accesorio_repository.delete(accesorio)
        return redirect('accesorios_list')

# Vista basada en clase para actualizar un accesorio
class AccesorioUpdateView(View):
    def get(self, request, pk):
        accesorio_repository = AccesorioRepository()
        accesorio = accesorio_repository.get_by_id(pk)
        form = AccesorioForm(instance=accesorio)
        return render(request, 'accesorios/accesorios_update.html', {'form': form})

    def post(self, request, pk):
        accesorio_repository = AccesorioRepository()
        accesorio = accesorio_repository.get_by_id(pk)
        form = AccesorioForm(request.POST, request.FILES, instance=accesorio)
        if form.is_valid():
            form.save()
            return redirect('accesorios_list')
        return render(request, 'accesorios/accesorios_update.html', {'form': form})

# Vista basada en clase para crear un nuevo accesorio
class AccesorioCreateView(View):
    def get(self, request):
        form = AccesorioForm()
        return render(request, 'accesorios/accesorios_create.html', {'form': form})

    def post(self, request):
        form = AccesorioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accesorios_list')
        return render(request, 'accesorios/accesorios_create.html', {'form': form})
