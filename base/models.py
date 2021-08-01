from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    def __str__(self):
        return self.title
    
class Skills(models.Model):
    title = models.CharField(max_length = 200)
    fonticon = models.CharField(max_length = 100, null=True)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    
    
    def __str__(self):
        return self.title


    
class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    
    
    def __str__(self):
        return self.name