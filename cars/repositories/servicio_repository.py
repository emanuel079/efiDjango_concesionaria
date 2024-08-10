from typing import List, Optional
from cars.models import Servicio

class ServicioRepository:
    def get_all(self) -> List[Servicio]:
        return Servicio.objects.all()

    def get_by_id(self, id: int) -> Optional[Servicio]:
        return Servicio.objects.filter(id=id).first()

    def create(self, nombre: str, descripcion: str, precio: float) -> Servicio:
        return Servicio.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)

    def delete(self, servicio: Servicio):
        return servicio.delete()
