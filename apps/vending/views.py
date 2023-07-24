from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.vending.models import VendingMachineSlot
from apps.vending.serializers import VendingMachineSlotSerializer
from apps.vending.validators import ListSlotsValidator
from apps.vending.services import format_slots_into_products_grid


class VendingMachineSlotView(APIView):
    def get(self, request: Request) -> Response:
        validator = ListSlotsValidator(data=request.query_params)
        validator.is_valid(raise_exception=True)
        filters = {}
        if quantity := validator.validated_data["quantity"]:
            filters["quantity__lte"] = quantity

        slots = VendingMachineSlot.objects.filter(**filters)
        slots_serializer = VendingMachineSlotSerializer(slots, many=True)
        return Response(data=slots_serializer.data)

class VendingMachineProductsView(APIView):
    def get(self, request: Request) -> Response:
        products_grid = format_slots_into_products_grid()
        # flatten the products grid
        products_list = []
        for sublist in products_grid:
            products_list.extend(sublist)
        return Response(data=products_list)
        