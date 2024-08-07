from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        User.objects.create_superuser(
            username='adminnola',
            password='Jibril120207'
            )
        print('Superuser has been created.')