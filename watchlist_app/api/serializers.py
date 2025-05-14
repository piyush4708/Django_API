from rest_framework import serializers
from watchlist_app.models import WatchList,StreamingPlatform


class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields  = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-Detail')
    class Meta:
        model = StreamingPlatform
        fields = "__all__"
# class WatchListSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = WatchList
#         # fields = "__all__" 
#         exclude = ["active"]
        
        # def validate(self, data):
        #     if data["name"] == data["description"]:
        #         raise serializers.ValidationError("Name should not be equal to description")
        #     return data
        
        # def validate_name(self,value):
        #     if len(value) < 2:
        #         raise serializers.ValidationError("Name is to Short!")
        #     else:
        #         return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description =  validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name should not be equal to description")
#         return data
    
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is to Short!")
#         else:
#             return value
            