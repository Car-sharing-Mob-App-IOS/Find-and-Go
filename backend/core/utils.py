import random

from django.conf import settings
from django.core.mail import send_mail

from core.texts import USER_RESET_CODE_LEN


def send_confirmation_code(email, code):
    """Функция отправки сообщений."""

    subject = "Сброс пароля"
    message = f"Ваш временный код для сброса пароля: {code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


def generate_reset_code():
    """Функция генерации кода."""

    code = "".join(
        [str(random.randint(0, 9)) for _ in range(USER_RESET_CODE_LEN)],
    )
    return code


def get_attempts_word(attempts):
    """Возвращает правильную форму слова "попытка" в зависимости от числа."""

    if attempts % 100 in {11, 12, 13, 14}:
        return "попыток"
    elif attempts % 10 == 1:
        return "попытка"
    elif 2 <= attempts % 10 <= 4:
        return "попытки"
    else:
        return "попыток"


def image_upload_to(instance, filename):
    """
    Метод класса Car, предназначенный для генерации пути
    сохранения изображения автомобиля.
    """
    return (
        f"cars/images/{instance.company}/{instance.brand}_"
        f"{instance.model}/{filename}"
    )
