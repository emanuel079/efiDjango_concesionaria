from django.urls import path
from users.views import RegisterView, AdminRegisterView , StaffView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('admin_register/', AdminRegisterView.as_view(), name='admin_register'),
    path('staff/', StaffView.as_view(), name='staff'),  

]
