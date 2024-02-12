
from .views import LessonViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', LessonViewSet)


urlpatterns = [

]


urlpatterns+=router.urls
