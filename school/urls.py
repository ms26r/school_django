from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/person/',include('person.urls')),
    path('api/category-lesson/',include('category_lesson.urls')),
    path('api/category_lesson_content/',include('category_lesson_content.urls')),
    path('api/lesson/',include('lesson.urls')),
    # path('api/lesson-student/',include('lesson_students.urls')),
    path('api/lesson-content/',include('lesson_content.urls')),
    path('api/lesson-practice/',include('lesson_practice.urls')),
]
