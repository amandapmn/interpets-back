from rest_framework import serializers
from interpets2019.models import Petiano


class PetianoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Petiano
        fields = ('nome', 'email', 'telefone', 'restricao_alimentar', 'pet', 'oficina')