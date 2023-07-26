from rest_framework.views import exceptions

from apps.vending.models import User
from apps.vending.validators import ProfilePartialUpdateRequestDTO


class UpdateProfileUseCase:

    def execute(self, id, data: ProfilePartialUpdateRequestDTO):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise exceptions.ValidationError(detail='No user found with this id!')
        print("Updating profile attributes")
        # Updating just balance for the moment
        user.balance = data.balance if data.balance is not None else user.balance
        user.save()
        return user