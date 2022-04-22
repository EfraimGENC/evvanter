from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from evvanter.core.models import BaseModel


class Location(BaseModel):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    class Meta(BaseModel.Meta):
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)


class Category(BaseModel):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    class Meta(BaseModel.Meta):
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)


class Label(BaseModel):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    class Meta(BaseModel.Meta):
        verbose_name = _('label')
        verbose_name_plural = _('labels')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)


class Brand(BaseModel):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    class Meta(BaseModel.Meta):
        verbose_name = _('brand')
        verbose_name_plural = _('brand')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)


class Document(BaseModel):
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE, verbose_name=_('inventory'))
    title = models.CharField(_('title'), max_length=255)
    # file = models.FileField(_('file'), upload_to='documents')

    class Meta(BaseModel.Meta):
        verbose_name = _('document')
        verbose_name_plural = _('documents')


class Image(BaseModel):
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE, verbose_name=_('inventory'))
    title = models.CharField(_('title'), max_length=255)
    # image =

    class Meta(BaseModel.Meta):
        verbose_name = _('image')
        verbose_name_plural = _('images')


class Inventory(BaseModel):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    cost = models.DecimalField(_('cost'), max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(_('quantity'))
    location = models.ForeignKey('inventory.Location', on_delete=models.PROTECT, verbose_name=_('location'))
    category = models.ForeignKey('inventory.Category', on_delete=models.SET_NULL, verbose_name=_('category'), null=True, blank=True)
    label = models.ForeignKey('inventory.Label', on_delete=models.SET_NULL, verbose_name=_('label'), null=True, blank=True)
    brand = models.ForeignKey('inventory.Brand', on_delete=models.SET_NULL, verbose_name=_('brand'), null=True, blank=True)
    serial = models.CharField(_('serial number'), max_length=255, null=True, blank=True)
    date_of_acquisition = models.DateField(_('date of acquisition'), null=True, blank=True)
    warranty_start = models.DateField(_('warranty start'), null=True, blank=True)
    warranty_finnish = models.DateField(_('warranty finnish'), null=True, blank=True)

    class Meta(BaseModel.Meta):
        verbose_name = _('inventory')
        verbose_name_plural = _('inventories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)