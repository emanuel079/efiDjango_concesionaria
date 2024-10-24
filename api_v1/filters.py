import django_filters

from cars.models import Auto

class AutoFilter(django_filters.FilterSet):
    categoria = django_filters.CharFilter(
        field_name='categoria__nombre',
        lookup_expr='icontains'
    )

    class Meta:
        model = Auto
        fields = ['categoria',]