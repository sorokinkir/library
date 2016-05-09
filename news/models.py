from django.db import models


class News(models.Model):
    """Класс новостей"""
    title = models.CharField("Заголовок", max_length=100)
