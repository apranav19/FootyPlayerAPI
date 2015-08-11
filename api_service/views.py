from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api_service.models import FootballPlayer
from api_service.serializers import FootballPlayerSerializer

class JSONResponse(HttpResponse):
    '''
    This class provides a HTTP Response in the form of a JSON string
    '''
    def __init__(self, data, **kwargs):
        result = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(result, **kwargs)

def get_players(request):
    '''
    Fetches all players from the db and renders them in a JSON response
    '''
    if request.method == 'GET':
        players = FootballPlayer.objects.all()
        serializer = FootballPlayerSerializer(players, many=True) # Serialize a list of players
        return JSONResponse(serializer.data)
