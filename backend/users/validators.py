from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext as _


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


class MaximumLengthValidator(MinLengthValidator):
    def __init__(self, max_length=18):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _(
                    "Максимальная длина пароля - "
                    f"{self.max_length} символов."
                    ),
                code="password_too_long",
                params={"max_length": self.max_length},
            )

    def get_help_text(self):
        return _(
            "Максимальная длина пароля - "
            f"{self.max_length} символов."
        )
