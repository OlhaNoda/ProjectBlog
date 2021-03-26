from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url tag', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url category', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class News(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url news', unique=True)
    details = models.TextField()
    author = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True, related_name='news')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='news')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-date']
