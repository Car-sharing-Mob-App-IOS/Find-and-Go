import os

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core.serializers.base import DeserializationError


class Command(BaseCommand):
    file_paths = [
        os.path.join("cars/data", "new_cars.json"),
    ]

    def handle(self, *args, **options):
        options["verbosity"] = 0
        self.load_fixtures()

    def load_fixtures(self):
        for path in self.file_paths:
            try:
                call_command("loaddata", path, verbosity=0)
                self.stdout.write(
                    self.style.SUCCESS(f"Данные из {path} успешно загружены.")
                )
            except (
                DeserializationError,
                FileNotFoundError,
                ValueError,
            ) as error:
                self.stdout.write(
                    self.style.ERROR(
                        f"Ошибка в загрузке. {error}. "
                        f"Не удалось загрузить данные из {path}."
                    )
                )
