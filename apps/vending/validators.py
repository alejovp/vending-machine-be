from dataclasses import dataclass
from rest_framework import serializers


@dataclass(frozen=True)
class ProfilePartialUpdateRequestDTO:
    username: serializers.CharField(required=False, default=None)
    balance: serializers.DecimalField(required=False, max_digits=6, decimal_places=2, default=None)

class ProfilePartialUpdateRequestValidator(serializers.Serializer):
    username = serializers.CharField(required=False, max_length=120)
    balance = serializers.DecimalField(max_digits=6, decimal_places=2, default=None, required=False)

    def build_dto(self) -> ProfilePartialUpdateRequestDTO:
        data = self.validated_data
        return ProfilePartialUpdateRequestDTO(
            username=data.get("username"),
            balance=data.get("balance"),
        )

class ListSlotsValidator(serializers.Serializer):
    quantity = serializers.IntegerField(required=False, min_value=0, default=None)