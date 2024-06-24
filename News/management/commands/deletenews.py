from django.core.management.base import BaseCommand, CommandError
from News.models import Post


class Command(BaseCommand):
    help = 'Delete all news by any category' # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True # напоминать ли о миграциях. Если true — то будет напоминание о том, что не сделаны все миграции (если такие есть)
    

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer =  input() # считываем подтверждение 
        
        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Post.objects.get(name=options['category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}')) # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {category.name}'))