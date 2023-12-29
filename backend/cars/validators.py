from django.core.validators import RegexValidator

from rest_framework import serializers

from core.texts import CAR_STATE_NUMBER_VALIDATOR_MESSAGE


def validate_state_number(value):
    """Валидатор для проверки корректности формата
    государственного номера автомобиля."""

    state_number_validator = RegexValidator(
        regex=r"^[а-яА-Я]{1}\d{3}[а-яА-Я]{2}\d{2,3}$",
        message=CAR_STATE_NUMBER_VALIDATOR_MESSAGE,
    )
    state_number_validator(value)


def state_number_validate(value, instance=None):
    """
    Проверка уникальности номера состояния.
    """
    from cars.models import Car

    if instance and instance.state_number == value:
        # Номер остался прежним, валидацию не проводим
        return value

    queryset = (
        Car.objects.exclude(pk=instance.pk) if instance else Car.objects.all()
    )

    if queryset.filter(state_number=value).exists():
        raise serializers.ValidationError(
            "Автомобиль с таким номером уже существует."
        )
    return value
