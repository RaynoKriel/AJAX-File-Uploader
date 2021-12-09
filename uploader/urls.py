from django.urls import path

from .views import uploadview

app_name = 'uploader'
urlpatterns = [
    path('', uploadview, name='uploadview'),
]
