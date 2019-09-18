from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
class Post(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=255, verbose_name='titulo')
    subtitle = models.CharField(max_length=255 ,null= True, blank=True, verbose_name='subtitulo')
    content = models.TextField(verbose_name='conteudo')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Autor')
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
