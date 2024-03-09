from rest_framework import serializers

from .models import HeroSection


class HeroSectionSerializer(serializers.ModelSerializer):
   class Meta:
      model = HeroSection
      fields = ["id", "title", "job_title", "title_description"]
