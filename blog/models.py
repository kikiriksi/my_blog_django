from django.db import models
from users.models import CustomUser
import datetime


# Create your models here.
class Post(models.Model):
    '''Таблица постов'''
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    descriptions = models.TextField(verbose_name='Текст записи')
    date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(verbose_name='Изображение', upload_to='image_blog')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}, {self.user}'

    class Meta:
        verbose_name = 'Запись'  # отвечает за отображения имя таблицы
        verbose_name_plural = 'Записи'


class CommentsModel(models.Model):
    '''Коментарий'''
    comments = models.TextField(verbose_name='Коментарий', max_length=2000)
    post = models.ForeignKey(Post, verbose_name="Публикации", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comments}'

    class Meta:
        verbose_name = 'Коментарий'  # отвечает за отображения имя таблицы
        verbose_name_plural = 'Коментарии'
