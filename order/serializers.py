from rest_framework import serializers

from booking.models import BookingDetail
# from booking.serializers import BookingDetailSerializer
from order.models import Order, Service


class ServiceSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    booking_detail_id = serializers.PrimaryKeyRelatedField(queryset=BookingDetail.objects.all(),
                                                           source='booking_detail',
                                                           write_only=True)

    # booking_detail = BookingDetailSerializer(read_only=True)

    service = ServiceSerializer(many=True, read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), source='service',
                                                    write_only=True, many=True)

    service_cost = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    class Meta:
        model = Order
        fields = '__all__'
