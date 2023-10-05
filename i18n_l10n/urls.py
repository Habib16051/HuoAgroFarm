from django.urls import path
from . import views


# app_name = 'i18n_l10n'

urlpatterns = [
    path('local/', views.Local_Language, name='local')
    
]
