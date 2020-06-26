from django_filters import rest_framework as filters
from .models import Event


class EventFilter(filters.FilterSet):
	date_gte = filters.IsoDateTimeFilter(field_name='date', lookup_expr='gte')
	date_lte = filters.IsoDateTimeFilter(field_name='date', lookup_expr='lte')

	class Meta:
		model = Event
		fields = ['name', 'category__category_name', 'status', 'place', 'date_gte', 'date_lte']

		# fields = {
		# 	'name': ['exact', 'icontains'],
		# 	'category__category_name': ['exact', 'icontains'],
		# 	'status': ['exact', ],
		# 	'place': ['exact', 'icontains'],
		# }
