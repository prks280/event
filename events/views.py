from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from .filters import EventFilter
from .models import EventCategory, Event, EventPhoto
from .serializers import EventSerializer, EventCategorySerializer, EventPhotoSerializer


class EventCategoryViewSet(viewsets.ModelViewSet):
	queryset = EventCategory.objects.all()
	serializer_class = EventCategorySerializer


class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
	search_fields = ['name', 'event_id']
	ordering_fields = ['id', 'name', 'place', 'status', 'category__category_name', 'date']
	filter_class = EventFilter


class EventPhotoViewSet(viewsets.ModelViewSet):
	queryset = EventPhoto.objects.all()
	serializer_class = EventPhotoSerializer

# class TestEventViewSet(viewsets.ModelViewSet):
# 	queryset = Event.objects.all()
# 	serializer_class = EventSerializer
#
# 	def get_queryset(self):
# 		return Event.objects.all()
#
# 	@action(detail=False, methods=['delete'])
# 	def multi_delete(self, request, *args, **kwargs):
# 		data = self.get_queryset()
# 		ser = self.get_serializer()(data)
# 		return ser
