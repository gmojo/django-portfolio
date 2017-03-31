from django.db import models
from django.utils import timezone

class Projects(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, default='moon.jpg')
    slug = models.SlugField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Projects'
