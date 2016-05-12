from django.db import models
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


class News(models.Model):
    """Класс новостей"""
    title = models.CharField("Заголовок", max_length=100)
    content = RichTextField("Новость")
    slug = models.SlugField("Поле для url", help_text="Пример: 'eto-pervay-novosty', Так же поле должно быть уникально",
                            unique=True)
    is_active = models.BooleanField("Показать новость")
    create_date = models.DateTimeField("Время создания", auto_now_add=True)
    mod_date = models.DateTimeField("Время редактирования", auto_now=True)

    def get_absolute_url(self):
        return reverse(News, kwargs={'slug': self.slug})

    class Meta:
        ordering = ["-create_date"]
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
