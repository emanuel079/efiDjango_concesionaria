from datetime import datetime
import pytz
import requests
from users.models import Profile
from django.core.exceptions import ObjectDoesNotExist

def profile(request):
    profile = None  # Inicializa como None por defecto
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            # Si el perfil no existe, simplemente deja `profile` como None
            profile = None  # O puedes optar por crear un nuevo perfil aquí si lo deseas
    return {'profile': profile}

def dolar_rate(request):
    # URL de la API para obtener la cotización del dólar
    api_url = 'https://api.exchangerate-api.com/v4/latest/USD'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza un error para códigos de estado HTTP que indiquen error
        data = response.json()

        # Verifica que la clave 'rates' y 'ARS' estén en los datos de la API
        if 'rates' in data and 'ARS' in data['rates']:
            usd_to_ars = data['rates']['ARS']  # Tasa de cambio de USD a ARS
        else:
            usd_to_ars = 'Datos no disponibles'
    except requests.exceptions.RequestException as e:
        # Manejo de errores de conexión o HTTP
        usd_to_ars = 'Error de conexión'
    except KeyError:
        # Manejo de errores si no se encuentra la clave 'rates' o 'ARS'
        usd_to_ars = 'Datos no disponibles'
    except Exception as e:
        # Otro manejo de errores generales
        usd_to_ars = 'Error al obtener cotización'

    return {
        'usd_to_ars': usd_to_ars
    }
def world_clock(request):
    # Definir las zonas horarias de interés
    timezones = {
        'Argentina': 'America/Argentina/Buenos_Aires',
        'Chile': 'America/Santiago',
        'Colombia': 'America/Bogota',
        'España': 'Europe/Madrid',
    }

    # Obtener la hora actual en cada zona horaria
    current_times = {}
    for country, tz in timezones.items():
        # Obtener la zona horaria usando pytz
        timezone = pytz.timezone(tz)
        # Obtener la hora actual en la zona horaria específica
        current_time = datetime.now(timezone)  # Usa datetime.now() con la zona horaria
        # Formatear la hora actual
        current_times[country] = current_time.strftime('%H:%M:%S')

    return {
        'world_clock': current_times
    }