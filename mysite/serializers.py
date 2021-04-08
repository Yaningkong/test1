from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
#创建serializer
from mysite.models import Text
from drf_haystack.serializers import HaystackSerializer

class TextSerializer(ModelSerializer):
    #指定序列化的model和fields
    class Meta:
        model = Text
        fields = '__all__'
class TestIndexSerializer(HaystackSerializer):
    object = TextSerializer(read_only=True)
    class Meta:
        index_classes=[Text]
        fields=("id","contents")
