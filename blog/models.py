from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(
        max_length=160,
        blank=False,
        null=False)
    date = models.DateField(
        blank=False,
        null=False)
    content = models.TextField(
        blank=False)

    class Meta:
        ordering = ['-date']

    @property
    def detail_url(self):
        return reverse('blog-detail', kwargs={'post_id': self.pk})
