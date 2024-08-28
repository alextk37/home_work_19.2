from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Создает группу модератора"

    def handle(self, *args, **kwargs):
        moderator_group, created = Group.objects.get_or_create(name="Moderator")

        can_change_is_published = Permission.objects.get(
            codename="can_change_is_published"
        )
        can_change_product_description = Permission.objects.get(
            codename="can_change_product_description"
        )
        can_change_product_category = Permission.objects.get(
            codename="can_change_product_category"
        )

        moderator_group.permissions.add(
            can_change_is_published,
            can_change_product_description,
            can_change_product_category,
        )

        self.stdout.write(self.style.SUCCESS("Группа модераторов успешно создана"))
