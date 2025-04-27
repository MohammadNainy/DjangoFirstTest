from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html

# MyManager

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status = 'p')

class CatrgoryManager(models.Manager):
    def active(self):
        return self.filter(status = True)


# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='children',verbose_name='زیر دسته')
    title = models.CharField(max_length=200,verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100,unique=True,verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True,verbose_name="آیا نمایش داده شود؟" )
    position = models.IntegerField(verbose_name="پوزیشن")
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title
    
    objects = CatrgoryManager()

class Article(models.Model):
    STATUS_CHOICE = (
        ('d',"پیشنویس"),
        ('p',"منتشر شده")
    )
    title = models.CharField(max_length=200,verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100,unique=True,verbose_name="اسلاگ")
    category = models.ManyToManyField(Category,verbose_name="دسته بندی",related_name="articles")
    describtion = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="",verbose_name="تصویر اصلی")
    publish = models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True,verbose_name="نویسنده مقاله")
    updated = models.DateTimeField(auto_now=True,verbose_name="زمان بروزرسانی")
    status = models.CharField(max_length=1, choices=STATUS_CHOICE,verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']
    

    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def thumbnail_tag(self):
        return format_html("<img width=75 height=45 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس مقاله"


    def category_published(self):
        return self.category.filter(status = True)
    
    objects = ArticleManager()