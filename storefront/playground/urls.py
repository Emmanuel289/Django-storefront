from django.urls import path

from . import views

# URLConf --> a url configuration module
urlpatterns = [
   path('hello/', views.say_hello),
   path('', views.say_hello_root)
]