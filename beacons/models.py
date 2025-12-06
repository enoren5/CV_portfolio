from django.db import models

# Create your models here.

class AuthToggle(models.Model):
    email = models.EmailField(max_length=50, default='')
    linkedin = models.CharField(max_length=50, default='')
    github = models.CharField(max_length=50, default='')
    stackoverflow = models.CharField(max_length=50, default='')

    def __str__(self):
        return "Options"

class Content(models.Model):
    title = models.CharField(max_length=30,blank=True)
    preamble_summary = models.TextField(max_length=300000,blank=True)
    about = models.TextField(max_length=300000,blank=True)
    # testimonial_carousel = models.TextField(max_length=300000,blank=True)  # JS/TS # hard coded?
    cms_samples = models.TextField(max_length=300000,blank=True)             # (x2) rota + hypno
    # book_lists = models.TextField(max_length=300000,blank=True)            # images with blurbs # hard coded?
    # udemy_courses_complete = models.TextField(max_length=300000,blank=True)# images with blurbs # hard coded?
    # vegan_meal_time = models.TextField(max_length=300000,blank=True)       # images with blurbs # hard coded?
    machine_learning_samples = models.TextField(max_length=300000,blank=True)# Jupyter Notebook
    algorithms = models.TextField(max_length=300000,blank=True)              # Jupyter Notebook
    documentation_samples = models.TextField(max_length=300000,blank=True)  
    aTimeLogger = models.TextField(max_length=300000,blank=True)             # Jupyter Notebook
    further_research_forwards = models.TextField(max_length=300000,blank=True)
        
    def __str__(self):
        return f'{self.title}'
        