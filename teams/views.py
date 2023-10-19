from rest_framework.views import APIView, status, Request, Response
from teams.models import Team
from django.forms.models import model_to_dict
from teams.utils import data_processing
from teams.utils import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()

        teams_dict = []

        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)
        return Response(teams_dict, status.HTTP_200_OK)
    
    def post(self, request: Request):
        try:
            data_processing(request.data)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"error": err.args[0]}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED) 


class TeamViewId(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)
    
    def patch(self, request: Request, team_id):
        try:
            team = Team.objects.get(pk=team_id)     
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team.name = request.data.get("name", team.name)
        team.titles = request.data.get("titles", team.titles)
        team.top_scorer = request.data.get("top_scorer", team.top_scorer)
        team.fifa_code = request.data.get("fifa_code", team.fifa_code)
        team.first_cup = request.data.get("first_cup", team.first_cup)

        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK) 
    
    def delete(self, request: Request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)