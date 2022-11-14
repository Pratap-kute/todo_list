from django.db import models
from django.urls import reverse
from django.utils import timezone


def one_week_hence():
    """
    Returns a date 1 week in the future.
    """
    return timezone.now() + timezone.timedelta(weeks=1)


class TodoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("todo_app:list", args=[self.id])

    def __str__(self) -> str:
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "todo_app:item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self) -> str:
        return f"{self.title}: due ({self.due_date})"

    class Meta:
        ordering = ["due_date"]
