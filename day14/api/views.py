from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

#for basic authentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #for authintication and permission
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

