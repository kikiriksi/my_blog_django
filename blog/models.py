from django.db import models


# Create your models here.
class Post(models.Model):
    '''Таблица постов'''
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    descriptions = models.TextField(verbose_name='Текст записи')
    author = models.CharField(verbose_name='Автор', max_length=25)
    date = models.DateField(verbose_name='Дата публикации')
    image = models.FileField(verbose_name='Изображение', upload_to='image_blog')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'  # отвечает за отображения имя таблицы
        verbose_name_plural = 'Записи'
