from rest_framework.viewsets import ModelViewSet

from api.models import HeroSection
from api.serializers import HeroSectionSerializer


class HeroSectionViewSet(ModelViewSet):
   queryset = HeroSection.objects.all()
   serializer_class = HeroSectionSerializer
