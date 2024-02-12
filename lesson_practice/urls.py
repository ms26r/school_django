
from .views import LessonPracticeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', LessonPracticeViewSet)


urlpatterns = [

]


urlpatterns+=router.urls
