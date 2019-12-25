# api/resources.py
from tastypie.resources import ModelResource
from api.models import Score
from tastypie.authorization import Authorization


class ScoreResource(ModelResource):
    class Meta:
        queryset = Score.objects.all()
        resource_name = 'score'
        authorization = Authorization()
