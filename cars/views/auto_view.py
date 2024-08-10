# views/auto_view.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cars.models import Auto

class AutoListView(ListView):
    model = Auto
    template_name = 'autos/auto_list.html'
    context_object_name = 'autos'

class AutoDetailView(DetailView):
    model = Auto
    template_name = 'autos/auto_detail.html'

class AutoCreateView(CreateView):
    model = Auto
    template_name = 'autos/auto_form.html'
    fields = ['modelo', 'categoria', 'precio', 'imagen', 'pais_fabricacion', 'conbustible', 'descripcion']
    success_url = reverse_lazy('auto_list')

class AutoUpdateView(UpdateView):
    model = Auto
    template_name = 'autos/auto_form.html'
    fields = ['modelo', 'categoria', 'precio', 'imagen', 'pais_fabricacion', 'conbustible', 'descripcion']
    success_url = reverse_lazy('auto_list')

class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'autos/auto_confirm_delete.html'
    success_url = reverse_lazy('auto_list')
