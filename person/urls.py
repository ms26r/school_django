from .views import PersonViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', PersonViewSet)


urlpatterns = [

]


urlpatterns+=router.urls
