from django.db import models
from django.contrib. auth .models import User
from datetime import date
from django.template.defaultfilters import slugify
from froala_editor.fields import FroalaField



class Blog(models.Model):
    name=models.CharField(max_length=100)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    description=FroalaField(help_text="write your blog")
    post_date=models.DateField(default=date.today)
    slug=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
       return self.name +"==> " + str(self.author)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name+"-"+str(self.post_date))
        return  super().save(*args,**kwargs)

class BlogCommment(models.Model):
    description=models.TextField(help_text="write your comment")
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    comment_date=models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return  str (self.blog) 
    

class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    e_mail =models.EmailField(max_length=250)
    phone_number=models.IntegerField()
    contact_message=models.TextField()
    timestamp=models.DateTimeField(auto_now=True,blank=True)
    
    def __str__(self):
        return str(self.first_name+" "+self.last_name)