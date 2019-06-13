from rest_framework import serializers
from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.api.serializers import RegistroHESerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHESerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ('id', 'nome', 'departamentos', 'empresa', 'user',
                  'total_horas_extras', 'registrohoraextra_set')


