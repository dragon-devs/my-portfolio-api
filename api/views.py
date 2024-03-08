from rest_framework import generics

from api.models import HeroSection
from api.serializers import HeroSectionSerializer


class HeroSectionListCreate(generics.ListCreateAPIView):
   queryset = HeroSection.objects.all()
   serializer_class = HeroSectionSerializer


class HeroSectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
   queryset = HeroSection.objects.all()
   serializer_class = HeroSectionSerializer
   lookup_field = "pk"
