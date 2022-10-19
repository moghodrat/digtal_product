from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categorise/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('categorise')



class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = _('product')
        verbose_name_plural = _('products')

class File(models.Model):
    product = models.ForeignKey('product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file = models.FileField(verbose_name=_('file'), upload_to='files/%y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'file'
        verbose_name = _('file')
        verbose_name_plural = _('files')
