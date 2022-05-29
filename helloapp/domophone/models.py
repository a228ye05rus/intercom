from django.db import models

class Product(models.Model):
    name = models.CharField('Наименование', max_length=60)
    short_desc = models.CharField('Краткое описание', max_length=250)
    full_desc = models.TextField('Полное описание', max_length=700)
    picture = models.ImageField('Предварительная просмотр', upload_to='product/', blank=True)
    price = models.PositiveSmallIntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары и услуги'
        verbose_name_plural = 'Товары и услуги'
