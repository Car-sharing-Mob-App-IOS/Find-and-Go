from django.core.validators import MinLengthValidator, RegexValidator


def name_surname_validator(value, min_length=3):
    """Validate name and surname."""
    validator = RegexValidator(
        regex=r"^[a-zA-Zа-яА-Я\-\–]+$",  # Добавлены тире и дефис
        message=("Неверное значение, допускаются только буквы без пробелов."),
    )
    min_length_validator = MinLengthValidator(
        limit_value=min_length,
        message=f"Значение поля должно быть "
        f"длиной не менее {min_length} символов.",
    )

    validator(value)
    min_length_validator(value)
