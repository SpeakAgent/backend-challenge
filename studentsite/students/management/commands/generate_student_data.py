from django.core.management.base import BaseCommand

from students.factories import SchoolFactory, StudentFactory, TeacherFactory


class Command(BaseCommand):
    help = "Generate random student data"

    def add_arguments(self, parser):
        parser.add_argument("--num-schools", "-s", default=5, type=int)
        parser.add_argument("--num-students", "-n", default=100, type=int)
        parser.add_argument("--num-teachers", "-t", default=30, type=int)

    def handle(self, *args, **options):
        schools = SchoolFactory.create_batch(options["num_schools"])
        teachers = TeacherFactory.create_batch(options["num_teachers"])
        StudentFactory.create_batch(options["num_students"], schools=schools, teachers=teachers)
