from rest_framework import serializers
from order.models import Order
from order.models import Shipping

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields = ['id', 'name', 'quantity', 'weigth', 'price', 'created_at']
        
        
        
    
    
class ShippingSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.IntegerField()
    
    class Meta:
        model = Shipping
        fields = ['id_reference', 'order', 'order_id', 'address', 'owner_name', 'owner_email', 'shipment_date', 'status']
        
    def create(self, validated_data):
        try:
            order = Order.objects.get(id=validated_data['order_id'])
            shipment = Shipping.objects.create(order=order, **validated_data)
            return shipment
        except Order.DoesNotExist:
            return serializers.ValidationError('This order does not exists') 