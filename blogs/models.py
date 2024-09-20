from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings
# Create your models here.

class Customer(models.Model):
    objects = models.Manager()


    name = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    mobile_no = models.CharField(max_length=10, null=True, blank=True)
    
    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    modified_on = models.DateField(default=datetime.now, editable=False)

    
    class Meta:
        verbose_name_plural = "Customer"
        verbose_name = "Customer"

    def __str__(self):
        return self.name


class BlogCategory(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        default=datetime.now, editable=False, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name



class Tags(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        default=datetime.now, editable=False, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name 


class Blog(models.Model):
    
    objects = models.Manager()

    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,limit_choices_to={'is_active':True})
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'blog-img/')
    descriptions = models.TextField()
    url = models.SlugField(editable=False)
    tags = models.ManyToManyField(Tags, null=True, blank=True)
    like = models.IntegerField(default=0)

    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        default=datetime.now, editable=False, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.name
    