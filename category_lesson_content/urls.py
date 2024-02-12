
from .views import CategoryLessonContentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', CategoryLessonContentViewSet)


urlpatterns = [

]


urlpatterns+=router.urls
