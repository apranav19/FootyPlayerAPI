from rest_framework import serializers
from api_service.models import FootballPlayer

class FootballPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballPlayer
        fields = ('id', 'first_name', 'last_name', 'age', 'club', 'country', 'position', 'kit_number')
