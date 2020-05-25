from rest_framework import routers,serializers,viewsets
from webapp.models import patient

class data1Serializer(serializers.ModelSerializer):
    class Meta:
        model=patient
        fields= '__all__'