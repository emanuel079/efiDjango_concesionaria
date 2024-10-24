from django.db import models

class AutoQuerySet (models.QuerySet):
    def actives(self):
        return self.filter(active=True)
    
    def inactives(self):
        return self.filter(active=False)

    def price_cars (self):
        total = 0
        for auto in self:
            total += auto.precio
        return total 
    
    def search_by_marca (self, marca_id):
        return self.filter(modelo__marca_id=marca_id)





    