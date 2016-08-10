from django.core.management.base import BaseCommand

from students.factories import StudentFactory


class Command(BaseCommand):
    help = "Generate random student data"

    def add_arguments(self, parser):
        parser.add_argument("--number", "-n", default=10, type=int)

    def handle(self, *args, **options):
        StudentFactory.create_batch(options["number"])
