from django.urls import path
from . import views


urlpatterns = [
    path('api/animals/data', views.get_animals_data ),
    path('api/animals/validate', views.validate_animals_response)
]
