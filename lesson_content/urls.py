
from .views import LessonContentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', LessonContentViewSet)


urlpatterns = [

]


urlpatterns+=router.urls
