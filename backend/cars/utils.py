from PIL import Image

from core.texts import TARGET_IMAGE_SIZE


def resize_image(image_path, target_size=TARGET_IMAGE_SIZE):
    """Сжимаем и сохраняем изображение до установленных значений."""
    try:
        image = Image.open(image_path)
        image = image.resize(target_size, resample=Image.LANCZOS)
        image.save(image_path)

    except Exception as e:
        print(f"Произошла ошибка при обработке изображения: {e}")
        return None


def image_upload_to(instance, filename):
    """
    Генерация пути сохранения изображения автомобиля.
    """
    upload_path = (
        f"cars/images/{instance.company}/"
        f"{instance.brand}_{instance.model}/{filename}"
    )
    return upload_path
