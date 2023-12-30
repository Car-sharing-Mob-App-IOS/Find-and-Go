import os

from PIL import Image

from core.texts import (
    TARGET_IMAGE_SIZE,
    LOAD_IMAGE_SIZE_KB,
    DEFAULT_QUALITY,
    QUALITY_REDUCTION_STEP,
)


def resize_image(
    image_path,
    target_size=TARGET_IMAGE_SIZE,
    max_file_size_kb=LOAD_IMAGE_SIZE_KB,
    default_quality=DEFAULT_QUALITY,
    quality_reduction_step=QUALITY_REDUCTION_STEP,
):
    image = Image.open(image_path)

    # Изменяем размер изображения
    image.thumbnail(target_size)

    # Сжимаем изображение с уменьшением качества,
    # чтобы уложиться в указанный размер файла
    while os.path.getsize(image_path) > max_file_size_kb * 1024:
        current_quality = image.info.get("quality", default_quality)
        new_quality = max(current_quality - quality_reduction_step, 0)

        if image.format == "PNG":
            image.save(image_path, "PNG", quality=new_quality, optimize=True)
        else:
            image.save(image_path, "JPEG", quality=new_quality, optimize=True)


def image_upload_to(instance, filename):
    """
    Генерация пути сохранения изображения автомобиля.
    """
    upload_path = (
        f"cars/images/{instance.company}/"
        f"{instance.brand}_{instance.model}/{filename}"
    )
    return upload_path
