
from .views import CategoryLessonViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', CategoryLessonViewSet)


urlpatterns = [

]


urlpatterns+=router.urls
