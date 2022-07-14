from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.employee.models import Employee
from apps.employee.serializers.serializers import EmployeeSerializer


class ListCreateEmployeeApiView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

