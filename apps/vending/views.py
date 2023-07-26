from uuid import UUID

from django.contrib.auth import login, logout, authenticate

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView, exceptions
from rest_framework import permissions, status

from apps.vending.models import VendingMachineSlot, User
from apps.vending.serializers import VendingMachineSlotSerializer, LoginSerializer
from apps.vending.validators import ListSlotsValidator, ProfilePartialUpdateRequestValidator
from apps.vending.services import format_slots_into_products_grid, DEFAULT_PASSWORD
from apps.vending.use_cases import UpdateProfileUseCase


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

class LoginView(APIView):

    # This view should be accessible also for unauthenticated users.
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, format=None):
        username = self.request.data['user_name']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username, DEFAULT_PASSWORD)

        user = authenticate(request, username=username, password=DEFAULT_PASSWORD)
        if user is not None:
            login(request, user)
            serialized_user = LoginSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):

    # This view should be accessible also for unauthenticated users.
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class ProfileView(APIView):

    def patch(self, request, id: UUID):
        validator = ProfilePartialUpdateRequestValidator(data=request.data)
        validator.is_valid(raise_exception=True)
        user = UpdateProfileUseCase().execute(id, validator.build_dto())
        return Response(data=LoginSerializer(user).data, status=status.HTTP_200_OK)