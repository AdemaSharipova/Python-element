from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from . import models
from . import serializers


class CategoriesView(ViewSet):

    def list(self, request, *args, **kwargs):
        categories = models.Category.objects.all()
        serializer = serializers.CategoryModelSerializer(categories, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        category = get_object_or_404(models.Category.objects.all(), pk=pk)
        serializer = serializers.CategoryModelSerializer(category)

        return Response(serializer.data)


class ProductsView(ViewSet):

    def list(self, request, *args, **kwargs):
        products = models.Product.objects.all()
        serializer = serializers.ProductModelSerializer(products, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        product = get_object_or_404(models.Product.objects.all(), pk=pk)
        serializer = serializers.ProductModelSerializer(product)

        return Response(serializer.data)

    def find_with_category(self, request, **kwargs):
        product = models.Product.objects.filter(category=kwargs['category_id'])
        serializer = serializers.ProductModelSerializer(product, many=True)

        return Response(serializer.data)

