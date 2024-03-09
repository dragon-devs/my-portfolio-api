from django.db import models


class HeroSection(models.Model):
   title = models.CharField(max_length=50, unique=True)
   job_title = models.CharField(max_length=50)
   title_description = models.CharField(max_length=100)
   about_me = models.TextField()
   experience_years = models.CharField(max_length=2)
   projects_completed_count = models.CharField(max_length=3)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.title
