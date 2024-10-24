from django.contrib.auth import (
    authenticate,
    login, 
    logout,
)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponseForbidden
from users.forms import UserRegisterForm, AdminUserRegisterForm
from users.utils import is_staff_user
from users.forms import AdminUserRegisterForm  # Asegúrate de que el formulario esté correctamente importado


def is_staff_user(user):
    return user.is_staff

class AdminRegisterView(View):
    form_class = AdminUserRegisterForm
    template_name = 'users/admin_register.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not is_staff_user(self.request.user):
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_superuser = True
            user.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(request, self.template_name, {'form': form})

# Define la vista StaffView
class StaffView(View):
    def get(self, request):
        # Renderiza la plantilla staff.html que muestra los botones para registrar usuarios y staff
        return render(request, 'users/staff.html') 


