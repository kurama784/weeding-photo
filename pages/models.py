#*-* coding: utf-8 *-*
from django.db import models
from solo.models import SingletonModel
from tinymce.models import HTMLField

class Contact(models.Model):

    STATUS_CHOICES = (
    ('YES', 'Succes'),
    ('NO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)

    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная Почта')
    place = models.CharField(max_length=50, verbose_name='Место съемки')
    length = models.IntegerField(verbose_name='Длительность сьемки')
    content = models.TextField(max_length=500)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявка'

class Settings(SingletonModel):
    site_name = models.CharField(max_length=30, verbose_name='Имя сайта',
                                 default='Weeding Photo - Kiev',
                                 help_text='Имя сайта')
    welcome = HTMLField(max_length=5000, verbose_name='Приветствие',
                        default='Ласкаво просимо на сайт, присвячений Весільної фотозйомці.Тут ви можете ознайомитися з нашим роботами, і замовити зйомку вашого весілля або просто фотосесію',
                        help_text= 'Приветствие на главной странице сайта',
                        blank=True,
                        null=True)

    background = models.ImageField(upload_to='images/', verbose_name='Фон',
                                   blank=True,
                                   null=True)
    logo = models.ImageField(upload_to='images/', verbose_name='Логотип', blank=True,
                             null=True)

    def __unicode__(self):

        return u"Настройки"

    class Meta:
        verbose_name = "Настройки"