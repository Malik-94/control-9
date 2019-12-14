from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Gallery(models.Model):
    images = models.ImageField(null=False, blank=False, verbose_name='Фото')
    signature = models.CharField(max_length=50, null=False, blank=False,verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    laike = models.PositiveIntegerField(default=0, verbose_name='Лайк')
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='Автор')


    def __str__(self):
        return self.author


    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='laike', on_delete=models.CASCADE, verbose_name='Автор лайка')
    images = models.ForeignKey('webapp.Gallery', related_name='like_received', null=False, blank=False, on_delete=models.CASCADE, verbose_name='Нравится фотография')

    def __str__(self):
        return self.images

class Comments(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    images = models.ForeignKey('webapp.Gallery', null=False, blank=False, on_delete=models.CASCADE, related_name='Comments', verbose_name='Фотография',)
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


    def __str__(self):
        return self.text[:20]


