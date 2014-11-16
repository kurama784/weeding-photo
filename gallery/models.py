#*-* coding: utf-8 *-*

from django.db import models
from gallery.controllers import upload_to
from sorl.thumbnail.shortcuts import get_thumbnail

class Album(models.Model):

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.CharField(max_length=500, verbose_name='Описание')
    client = models.CharField(max_length=40, verbose_name='Клиент')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(upload_to=upload_to, verbose_name='Фото')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Альбом'
        verbose_name_plural = u'Альбом'

class Photo(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(verbose_name="Фото",
                            upload_to="images/")
    album = models.ForeignKey(Album, verbose_name='Альбом')

    def get_thumbnail_html(self):
        img = self.image
        img_resize_url = unicode(get_thumbnail(img, '300x300').url)
        html = '<a class="image-picker" href="%s"><img src="%s"/></a>'
        return html % (self.image.url, img_resize_url)
    get_thumbnail_html.short_description = u'Миниатюра'
    get_thumbnail_html.allow_tags = True

    class Meta:
        verbose_name = u'Фото'
        verbose_name_plural = u'Фото'
