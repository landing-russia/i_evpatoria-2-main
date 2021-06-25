from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.safestring import mark_safe
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from i_evpatoria.models import TimeStampedModel


def excursions_photos_path(instance, filename):
    return 'excursions_photos/{0}/{1}/{2}/{3}'.format(datetime.now().year, datetime.now().month,
                                                      instance.excursion.slug, filename)


class Photo(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(
                "Максимальный размер файла %s MB" % str(megabyte_limit))

    name = models.CharField(max_length=100, default='Фото',
                            verbose_name='Подпись фото')
    excursion = models.ForeignKey(
        'Excursion', on_delete=models.CASCADE, related_name='photos', verbose_name='Экскурсия')
    image = models.ImageField(
        upload_to=excursions_photos_path, max_length=300, validators=[validate_image], verbose_name='Файл')

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="150" />'.format(self.image.url))
        else:
            return 'Нет фото'

    image_preview.short_description = 'Превью'

    def __str__(self):
        return self.excursion.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 1920, 1400

        if self.image:
            pic = Image.open(self.image.path)
            if pic.width > 1920 or pic.height > 1400:
                pic.thumbnail(SIZE, Image.LANCZOS)
                pic.save(self.image.path)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Excursion(TimeStampedModel):
    TYPES = (
        ('individual', 'Индивидуальная'),
        ('group', 'Групповая'),
    )
    guide = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='excursions', verbose_name='Гид')
    name = models.CharField(max_length=255, verbose_name='Название экскурсии')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Слаг', help_text='Заполняется автоматически')
    description = RichTextUploadingField(
        config_name='default', verbose_name='Описание')
    extra = RichTextUploadingField(
        config_name='mini', verbose_name='Дополнительная информация', blank=True)

    location = models.CharField(
        max_length=255, verbose_name='Локация', null=True, blank=True)
    duration = models.CharField(
        max_length=255, verbose_name='Длительность', null=True, blank=True)
    start_time = models.TimeField(
        blank=True, null=True, verbose_name='Время начала экскурсии')
    max_people_count = models.PositiveSmallIntegerField(
        verbose_name='Кол-во человек', null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='Стоимость для взрослых', null=True, blank=True)
    price_child = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='Стоимость для детей', null=True, blank=True)
    price_group = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='Стоимость для группы', null=True, blank=True)
    types = models.CharField(max_length=10, choices=TYPES,
                             verbose_name='Тип', default='individual')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    def first_image(self):
        return self.photos.first()

    def get_absolute_url(self):
        return reverse('excursions:excursion-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Экскурсию'
        verbose_name_plural = 'Экскурсии'
        ordering = ['-created']
