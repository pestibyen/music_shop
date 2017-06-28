from django.db import models

class News(models.Model):
    newsheader = models.CharField(max_length=50)
    newstext = models.TextField(default='')
    newsdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newsheader

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
