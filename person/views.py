from rest_framework import permissions, viewsets

from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('created_at')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
