from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

#for basic authentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #for authintication and permission
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

# #example....
# from rest_framework.permissions import AllowAny
# class StudentModelViewSet1(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # #for authintication and permission using specific permission
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]
