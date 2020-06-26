from django.db import models

EVENT_STATUS = ((True, 'Active'), (False, 'Inactive'))


class EventCategory(models.Model):
	category_name = models.CharField(max_length=20)

	def __str__(self):
		return self.category_name


class Event(models.Model):
	event_id = models.CharField(max_length=15, unique=True, blank=True)
	category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	date = models.DateTimeField(null=True, blank=True)
	place = models.CharField(max_length=10, null=True, blank=True)
	status = models.BooleanField(choices=EVENT_STATUS,)

	def __str__(self):
		return "event: {} category: {}".format(self.name, self.category)


class EventPhoto(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	image_file = models.ImageField(upload_to='media/')

