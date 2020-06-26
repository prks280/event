from rest_framework.routers import DefaultRouter

from .views import EventViewSet, EventCategoryViewSet, EventPhotoViewSet

event_routers = DefaultRouter()

event_routers.register('event_category', EventCategoryViewSet, basename='event_category')
event_routers.register('event', EventViewSet, basename='event')
event_routers.register('photo', EventPhotoViewSet, basename='photo')

urlpatterns = event_routers.urls


# curl -X POST -S  -H 'Accept: application/json'  -F "event=1"  -F "photo=@/home/cp/Desktop/1.png;type=image/png"  http://127.0.0.1:8000/photo/
# curl -X POST -S -H -u "cp:123" 'Content-Type: application/json' --data-binary '{"event":"1", "image":"@/home/cp/Desktop/1.png;type=image/png"}' http://127.0.0.1:8000/photo/