from typing import List, Optional
from cars.models import Venta, Auto, Accesorio, Cliente

class VentaRepository:
    def get_all(self) -> List[Venta]:
        return Venta.objects.all()

    def get_by_id(self, id: int) -> Optional[Venta]:
        return Venta.objects.filter(id=id).first()

    def create(self, auto: Auto, accesorio: Accesorio, cliente: Cliente, precio_final: float) -> Venta:
        return Venta.objects.create(auto=auto, accesorio=accesorio, cliente=cliente, precio_final=precio_final)

    def delete(self, venta: Venta):
        return venta.delete()
