from django.urls import path
from .views import PreferenceFormView

app_name = 'preference'

urlpatterns = [
    path('', PreferenceFormView.as_view(), name='main'),
]