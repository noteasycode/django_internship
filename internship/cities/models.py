from django.db import models
from pytils.translit import slugify


class Country(models.Model):
    name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=3)
    population = models.IntegerField()
    flag = models.ImageField(
        'Flag',
        upload_to='flags/',
        blank=True
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='cities'
    )
    population = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    emblem = models.ImageField(
        'Emblem',
        upload_to='emblems/',
        blank=True
    )
    with_mcdonalds = models.BooleanField()

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        super().save(*args, **kwargs)
