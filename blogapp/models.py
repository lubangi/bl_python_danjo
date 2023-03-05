#importing the models class from django
from django.db import models
#importing the timezone module that will allow us to get  the current time
from django.utils import timezone

# Create your models here.

#creating the first models class  for handing the blog post
class Post(models.Model): # declare a class named Post which heritate the mongo db model class

    class Status(models.TextChoices): #cretating the enum for managing the state of the post
        DRAFT = 'DF', "Draft" #first member of the enum
        PUBLISHED ='PB', 'Published' #second member of the enum

    title = models.CharField(max_length=250) #the title propeerty to store the blog title
    slug = models.SlugField(max_length=250) #the slug property to store the tags of the post
    body = models.TextField() #the body property to store the content of the blog post
    publish = models.DateField(default=timezone.now) # the publish property to store the publication date
    created = models.DateField(auto_now=True) # the created property to store the date of creation
    updated = models.DateField(auto_now=True) # the updated property to store the update date
    status = models.CharField(max_length=2,choices= Status.choices,default=Status.DRAFT) # the status property which works with the enum class Status  declared above

    # A subclass to store the sorting preference
    class Meta: # declaring the sub class with the name Meta for Metadata
        ordering = ['-publish'] #Defining the order column wich is publish, the - means the order will be reversed
        # creating the index on the publish column, again we use - to reverse the order
        indexes = [
            models.Index(fields=['-publish'])
        ]
    
    # defining the constructor, whenever a new object will be created, the class will return the title
    def __str__(self):
        return self.title
    
