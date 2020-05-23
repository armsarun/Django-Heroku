from django.urls import path

from sample import views

urlpatterns = [
  path('', views.index)
]
