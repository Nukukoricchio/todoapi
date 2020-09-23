from django.core.management.base import BaseCommand, CommandError

from todo.models import Todo


class Command(BaseCommand):
	help = "Create some demo todos"

	def handle(self, *args, **kwargs):
		try:
			Todo.objects.create(title='Build unitrack')
			Todo.objects.create(title='Build hacksoft')
			Todo.objects.create(title='Build todoAPIs')
			Todo.objects.create(title='Build Vue todoapp')
			Todo.objects.create(title='Learn machine learning')
		except:
			raise CommandError('Failed!!!')
