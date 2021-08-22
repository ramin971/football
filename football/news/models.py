from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    STATUS_CHOICES=(('d', 'پیشنویس'), ('p', 'انتشار'),)

    title=models.CharField(max_length=200,verbose_name='عنوان')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='آدرس url')
    description=models.TextField(verbose_name='توضیحات')
    thumbnail=models.ImageField(upload_to='images',verbose_name='تصویر')
    created=models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    publish=models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
    updated=models.DateTimeField(auto_now=True,verbose_name='زمان بروزرسانی')
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name='وضعیت')

    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'

    def __str__(self):
        return self.title