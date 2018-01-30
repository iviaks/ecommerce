from catalog.models import Product, Store
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'pk', 'store', 'title', 'image', 'price'
        )
        read_only_fields = fields


class ProductDetailsSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'pk', 'store', 'title',
            'image', 'description', 'price'
        )
        read_only_fields = fields


class StoreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('pk', 'name', 'image', 'products')
        read_only_fields = fields
