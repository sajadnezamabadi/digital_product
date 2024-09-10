from rest_framework import serializers

from .models import *

###########################

class CategorySerializers(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta :
        model =  Category
        fields = ('title' , 'description' , 'avatar')
        
    def get_file_type(self , obj):
        return obj.get_file_type_display()

class FileSerializers(serializers.ModelSerializer):
    class Meta :
        model =  File
        fields = ('id','title' ,'file', 'file_type')
        

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializers(many=True)
    files = FileSerializers(many=True)
    
    class Meta :
        model =  Product
        fields = ('id','title' ,'description' , 'avatar' , 'categories', 'files' , 'url')
        