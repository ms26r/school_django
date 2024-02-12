
from .views import LessonStudentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', LessonStudentsViewSet)


urlpatterns = [

]


urlpatterns+=router.urls
