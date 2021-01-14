import time

from django.core import management
from django import db


class Command(management.base.BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--collectstatic", action="store_true")
        parser.add_argument("--migrate", action="store_true")

    def handle(self, *args, **options):
        if options["collectstatic"]:
            management.call_command("collectstatic", interactive=False)
        if options["migrate"]:
            for _ in range(5):
                try:
                    db.connection.cursor()
                except db.utils.OperationalError as e:
                    err = e
                    time.sleep(2)
                else:
                    management.call_command("migrate")
                    break
            else:
                raise err
