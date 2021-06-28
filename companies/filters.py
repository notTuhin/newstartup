import django_filters

from .models import Companies

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Companies
        fields = '__all__'


 