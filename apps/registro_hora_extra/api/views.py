
from rest_framework import viewsets
from apps.registro_hora_extra.api.serializers import RegistroHESerializer
from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHEViewSet(viewsets.ModelViewSet):

    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHESerializer

