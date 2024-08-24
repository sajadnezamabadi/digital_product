from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey("self", verbose_name=_("parent"), blank= True,null= True , on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description") , blank= True)
    avatar = models.ImageField(_('avatar') , upload_to='categories/')
    is_enable = models.BooleanField(_('is enable') ,default=True)
    created_time = models.DateTimeField(_('create time ') ,auto_now_add=True)
    update_time = models.DateTimeField(_('update time') ,auto_now=True)
        
    class Meta:
        db_table = _('categories')
        verbose_name= _('Category')
        verbose_name_plural = _('Categories')
    
class Product(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description") , blank= True)
    avatar = models.ImageField(_('avatar') , upload_to='products/')
    is_enable = models.BooleanField(_('is enable') ,default=True)
    categories = models.ManyToManyField("Category", verbose_name=_("categories") , blank=True)
    created_time = models.DateTimeField(_('create time ') ,auto_now_add=True)
    update_time = models.DateTimeField(_('update time') ,auto_now=True)
    
    class Meta:
        db_table = _('products')
        verbose_name= _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey("Product", verbose_name=_("product"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    file = models.FileField(_("file"), upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_("is enable "), default= True)
    created_time = models.DateTimeField(_('create time ') ,auto_now_add=True)
    update_time = models.DateTimeField(_('update time') ,auto_now=True)
    
    class Meta:
        db_table = _('file')
        verbose_name= _('file')
        verbose_name_plural = _('files')
    