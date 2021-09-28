from rest_framework import fields, serializers
from order.models import Shop, Menu, Order, Orderfood

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        #fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        fields = '__all__'