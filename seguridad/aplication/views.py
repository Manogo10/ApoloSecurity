from rest_framework.decorators import permission_classes
from aplication.models import Usuario
from aplication.serializers import UsuarioSerializer
from aplication.permissions import IsPostOrIsAuthenticated
from rest_framework import generics


@permission_classes((IsPostOrIsAuthenticated, ))
class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
