from cars.models import Empleado

class EmpleadoRepository:
    def get_all(self):
        return Empleado.objects.all()

    def get_by_id(self, id):
        return Empleado.objects.get(id=id)

    def delete(self, empleado):
        empleado.user.is_staff = False  # Remueve el estado de staff si se elimina el empleado
        empleado.user.save()
        empleado.delete()
