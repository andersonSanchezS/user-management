from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Serializers
from auth_server.api.serializers.teams.index import TeamSerializer
# Models
from auth_server.api.models.teams.index import Team
# permissions
from rolepermissions.decorators import has_permission_decorator


@api_view(['GET'])
@has_permission_decorator('list_team')
def getTeams(request):
    try:
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response({'teams': serializer.data}, status=status.HTTP_200_OK)
    except teams.DoesNotExist:
        return Response({'message': 'Teams not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@has_permission_decorator('add_team')
def addTeam(request):
    try:
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
