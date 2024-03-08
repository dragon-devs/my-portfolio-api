from django.urls import path
from . import views
urlpatterns = [
    path("herosection/", views.HeroSectionListCreate.as_view(), name="herosection-view-create"),
    path("herosection/<int:pk>/", views.HeroSectionRetrieveUpdateDestroy.as_view(), name="update")
]
