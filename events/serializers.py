from rest_framework import serializers
from .models import *
from .utils import generate_event_id
from django.db import transaction


class EventCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = EventCategory
		fields = '__all__'


class EventPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = EventPhoto
		fields = '__all__'
		# read_only_fields = ('event',)


class EventSerializer(serializers.ModelSerializer):
	event_photos = EventPhotoSerializer(many=True, required=False)
	event_category = serializers.StringRelatedField(source='category.category_name')

	class Meta:
		model = Event
		fields = '__all__'
		read_only_fields = ('event_id',)

	@transaction.atomic
	def create(self, validated_data):
		event_id = generate_event_id()
		validated_data['event_id'] = event_id
		instance = super(EventSerializer, self).create(validated_data)

		# event_photos = validated_data.pop('event_photos')
		# for photo in event_photos:
		# 	photo = EventPhoto(event=instance, **photo)
		# 	EventPhoto.objects.create(photo)
		return instance
