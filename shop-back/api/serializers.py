from rest_framework import serializers

from . import models


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'