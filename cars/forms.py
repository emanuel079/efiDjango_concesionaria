from django import forms
from django.contrib.auth.models import User

from cars.models import Auto, Cliente, Comentario, Venta, Empleado, Proveedor, Servicio, Cita, Accesorio, Categoria, Marca, ModeloAuto

# Formulario para el modelo Auto
class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['modelo', 'categoria', 'precio', 'imagen', 'combustible', 'descripcion']
        widgets = {
            'modelo': forms.Select(attrs={'class': 'form-control custom-class'}),
            'categoria': forms.Select(attrs={'class': 'form-control custom-class'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control custom-class'}),
            'combustible': forms.TextInput(attrs={'class': 'form-control custom-class', 'placeholder': 'Tipo de combustible'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control custom-class'}),
        }
# Formulario para el modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:        
        model = Cliente
        fields = ['user', 'telefono', 'direccion']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control custom-class'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }

# Formulario para el modelo Comentario




class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']  # Incluye solo el campo de comentario
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control custom-class'}),
        }
        
# Formulario para el modelo Venta
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['auto', 'accesorio', 'cliente', 'precio_final']
        widgets = {
            'auto': forms.Select(attrs={'class': 'form-control custom-class'}),
            'accesorio': forms.Select(attrs={'class': 'form-control custom-class'}),
            'cliente': forms.Select(attrs={'class': 'form-control custom-class'}),
            'precio_final': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
        }


# Formulario para el modelo Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['user', 'puesto', 'imagen',]

    # Solo permitimos seleccionar usuarios que sean staff para promoverlos
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True),
        label='Usuario',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    puesto = forms.CharField(
        max_length=100,
        label='Puesto',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

# Formulario para el modelo Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'direccion', 'autos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'autos': forms.SelectMultiple(attrs={'class': 'form-control custom-class'}),
        }

# Formulario para el modelo Servicio
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control custom-class'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
        }

# Formulario para el modelo Cita
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['cliente','servicio', 'fecha', 'descripcion']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['cliente'].queryset = Cliente.objects.filter(user=user)

     
# Formulario para el modelo Accesorio
from django import forms
from .models import Accesorio

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ['nombre', 'descripcion', 'precio', 'autos', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control custom-class'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control custom-class'}),
            'autos': forms.SelectMultiple(attrs={'class': 'form-control custom-class'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control custom-class'}),
        }



# Formulario para el modelo Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }


# Formulario para el modelo Marca
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }


# Formulario para el modelo ModeloAuto
class ModeloAutoForm(forms.ModelForm):
    class Meta:
        model = ModeloAuto
        fields = ['nombre', 'marca']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'marca': forms.Select(attrs={'class': 'form-control custom-class'}),
            'anio': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }