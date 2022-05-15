from rest_framework.serializers import ModelSerializer
from .models import SurveyResponse

class SurveyResponsesSerializer(ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ['Data'] 