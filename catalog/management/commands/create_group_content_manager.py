from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Создает группу контент менеджера"

    def handle(self, *args, **kwargs):
        content_manager_group, created = Group.objects.get_or_create(
            name="ContentManager"
        )

        can_change_is_published = Permission.objects.get(
            codename="can_change_article_is_published"
        )
        can_change_description = Permission.objects.get(
            codename="can_change_article_description"
        )
        can_change_content = Permission.objects.get(
            codename="can_change_article_content"
        )
        can_change_preview_img = Permission.objects.get(
            codename="can_change_article_preview_img"
        )
        can_change_slug = Permission.objects.get(codename="can_change_article_slug")

        content_manager_group.permissions.add(
            can_change_is_published,
            can_change_description,
            can_change_content,
            can_change_preview_img,
            can_change_slug,
        )

        self.stdout.write(
            self.style.SUCCESS("Группа контент менеджера успешно создана")
        )
