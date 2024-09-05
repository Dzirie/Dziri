from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
    def __str__(self):
        return self.name


class Picture(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='pictures',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo_images',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='pictures',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
