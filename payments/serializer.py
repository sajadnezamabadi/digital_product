from rest_framework import serializers

from .models import *

#########################

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        models =  Gateway
        fields = ['id','title','description','avatar']