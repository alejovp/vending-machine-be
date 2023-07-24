from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=4, decimal_places=2)

class StockSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=0)

class VendingMachineSlotSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    quantity = serializers.IntegerField()
    coordinates = serializers.SerializerMethodField()
    product = ProductSerializer()

    def get_coordinates(self, instance) -> list[int, int]:
        return [instance.row, instance.column]