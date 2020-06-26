from .models import Event


def generate_event_id():
	prefix = 'EVENT#'
	last_event = Event.objects.all().last()
	if last_event:
		last_event_id = last_event.id
		return prefix + str(last_event_id + 1).zfill(4)
	return prefix + str(1).zfill(4)
