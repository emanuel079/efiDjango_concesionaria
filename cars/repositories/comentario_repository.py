from typing import List, Optional
from cars.models import Comentario, Auto, Cliente

class ComentarioRepository:
    def get_all(self) -> List[Comentario]:
        return Comentario.objects.all()

    def filter_by_id(self, id: int) -> Optional[Comentario]:
        return Comentario.objects.filter(id=id).first()

    
    def create(self, comentario: Comentario) -> Comentario:
        comentario.save()  # Asegúrate de que este paso está guardando el comentario
        return comentario


    def delete(self, comentario: Comentario):
        return comentario.delete()

    def filter_by_auto(self, auto: Auto) -> List[Comentario]:
        return Comentario.objects.filter(auto=auto)

    def filter_by_cliente(self, cliente: Cliente) -> List[Comentario]:
        return Comentario.objects.filter(cliente=cliente)

    def update(self, comentario: Comentario, data: dict):
        for field, value in data.items():
            setattr(comentario, field, value)
        comentario.save()
