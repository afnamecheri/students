from rest_framework import generics, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from django.db import IntegrityError


class Index(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JSONWebTokenAuthentication]

class Detail(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JSONWebTokenAuthentication]

class Add(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({"message": "Registration number already exists"}, status=status.HTTP_400_BAD_REQUEST)

class Edit(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JSONWebTokenAuthentication]
   

class Delete(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Successfully deleted"}, status=status.HTTP_200_OK)    
