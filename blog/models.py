from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
        	url = self.image.url
        except:
            url = ''
        return url    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = RichTextField(config_name="default",blank=True, null=True )
    content = RichTextField(config_name="Full_tool_bar",blank=True, null=True )
    image = CloudinaryField('image')
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
	
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ContactMessage(models.Model):
	name = models.CharField(max_length=200, null=False)
	email = models.CharField(max_length=200, null=False)
	message = models.TextField()

	def __str__(self):
		return self.name