from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='GarethMoger.com Blog')
    headimage = models.ImageField(default='stockblog1.jpeg')
    text = RichTextUploadingField()
    category = models.ForeignKey('Category')
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=150)
    tags = models.ManyToManyField(Tag)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
