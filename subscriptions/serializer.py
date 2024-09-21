from rest_framework import serializers

from .models import *

###########################

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        models = Package
        fields = ('title','sku','description','avatar','price','duration')
    

class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()
    
    class Meta:
        models = Subscription
        fields = ('package','create_time','expire_time')