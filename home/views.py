from django.contrib.auth import (
    authenticate,
    login, 
    logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View
from users.forms import UserRegisterForm
from users.models import Profile
from django.utils.translation import (
    activate,
    get_language,
    gettext_lazy as _,
)



# Create your views here.
class LoginView(View):

    def get(self, request):
        return render(
            request,
            'home/login.html'
        )
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')
        
class UpdateLang(View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        lang = profile.language
        if lang == 'es':
            profile.language = 'en'
        if lang == 'en':
            profile.language = 'es'
        profile.save()
        return redirect(request.META.get('HTTP_REFERER', 'index'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')



@login_required(login_url='login')
def index_view(request):
    return render(
        request,
        'home/index.html'
    )
    




