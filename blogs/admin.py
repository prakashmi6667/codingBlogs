from django.contrib import admin
from .models import BlogCategory,Blog, Tags, Customer
from django.utils.text import slugify
import os
# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_by','created_on','is_active']
    
    def save_model(self,request,obj,form,change):
        obj.created_by = request.user
        super().save_model(request,obj,form,change)

class TagsAdmin(admin.ModelAdmin):
    list_display = ['name','created_by','created_on','is_active']
    
    def save_model(self,request,obj,form,change):
        obj.created_by = request.user
        super().save_model(request,obj,form,change)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name',"email",'password','created_by','created_on','is_active']
    
    def save_model(self,request,obj,form,change):
        obj.created_by = request.user
        super().save_model(request,obj,form,change)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name','category','url','image','created_by','created_on','is_active']

    def delete_model(self, request, obj):
        try:
            os.remove(obj.image.path)
            super().delete_model(request, obj)
        except Exception as er:
            print(er)
    
    def save_model(self,request,obj,form,change):
        obj.url = slugify(obj.name)
        obj.created_by = request.user
        if change:
                imgData = Blog.objects.get(pk=obj.id)
                if imgData.image != obj.image:
                    if os.path.exists(imgData.image.path):
                        os.remove(imgData.image.path)

        super().save_model(request,obj,form,change)
        
admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Customer,CustomerAdmin)
