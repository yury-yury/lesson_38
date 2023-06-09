# Generated by Django 4.2 on 2023-06-01 04:03

from django.db import migrations, transaction
from django.utils import timezone


def create_objects(apps, schema_editor) -> None:
    """
    The create_objects function takes an application object as arguments. Creates new Board objects for each user
    located in the database, and fixes all existing categories on the created boards in accordance with the author.
    """
    User = apps.get_model("core", "User")
    Board = apps.get_model("goals", "Board")
    BoardParticipant = apps.get_model("goals", "BoardParticipant")
    GoalCategory = apps.get_model("goals", "GoalCategory")

    with transaction.atomic():
        for user in User.objects.all():
            new_board = Board.objects.create(
                title="Мои цели",
                created=timezone.now(),
                updated=timezone.now()
            )
            BoardParticipant.objects.create(
                user=user,
                board=new_board,
                role=1,
                created=timezone.now(),
                updated=timezone.now()
            )

            GoalCategory.objects.filter(user=user).update(board=new_board)


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_board_goalcategory_board_boardparticipant'),
    ]

    operations = [migrations.RunPython(create_objects)]
