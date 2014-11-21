#*-* coding: utf-8 *-*
from django.db import models
from solo.models import SingletonModel
from tinymce.models import HTMLField

class Contact(models.Model):

    STATUS_CHOICES = (
    ('в обработке', 'В обработке'),
    ('рассматривается', 'Рассматривается'),
    ('обработан', 'Обработан'),
    ('выполнен', 'Выполнен'),
)

    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная Почта')
    place = models.CharField(max_length=50, verbose_name='Место съемки')
    length = models.IntegerField(verbose_name='Длительность сьемки(часов)')
    content = models.TextField(max_length=500, verbose_name='Комментарии')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена(грн)')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')

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
    autoload_photos = models.BooleanField(default=False, verbose_name='Бесконечная загрузка фотографий(Тест)',
                                          help_text='При загрузке страницы фотографий они автоматически подгрузятся при скроллинге')
    fancybox = models.BooleanField(default=True,
                                  verbose_name='Просмотр фото в режиме галереи(только при отключенной автозагрузке)',
                                  help_text='При клике на фото будет включен режим галерии')

    def __unicode__(self):

        return u"Настройки"

    class Meta:
        verbose_name = "Настройки"