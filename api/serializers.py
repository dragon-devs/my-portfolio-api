from rest_framework import serializers
from .models import HeroSection


class HeroSectionSerializer(serializers.ModelSerializer):
   class Meta:
      model = HeroSection
      fields = ["title", "job_title", "title_description", "about_me", "experience_years", "projects_completed_count"]

