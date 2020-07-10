from django.db import models


class Command(models.Model):
    class Meta:
        ordering = ["priority"]

    name = models.CharField("Команда", max_length=32)
    help_text = models.CharField("Текст помощи", max_length=256, null=True)
    code = models.TextField("Код, который будет выполняться")
    priority = models.IntegerField("Приоритет", default=0)

    def __str__(self):
        return self.name
