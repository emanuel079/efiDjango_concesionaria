from typing import List, Optional
from cars.models import Accesorio, Auto

class AccesorioRepository:
    def get_all(self) -> List[Accesorio]:
        return Accesorio.objects.all()

    def get_by_id(self, id: int) -> Optional[Accesorio]:
        return Accesorio.objects.filter(id=id).first()

    def create(self, nombre: str, descripcion: str, precio: float, autos: List[Auto]) -> Accesorio:
        accesorio = Accesorio.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        accesorio.autos.set(autos)
        return accesorio

    def delete(self, accesorio: Accesorio):
        return accesorio.delete()
