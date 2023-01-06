from rest_framework import generics

from employee.models import Administrator
from employee.serializers import AdministratorSerializer


class BaseConfigurationAdministratorsViewGeneric(generics.GenericAPIView):
    serializer_class = AdministratorSerializer
    queryset = Administrator.objects.all()
