from django.urls import path
from . import views

# url configuration
# every view has it's own url configutation
# path() - this returns an url patter. Here we have provided the url of 'playground/helo'
#        - also we have provided the function which will handle this request from this url 'views.say_hello'

urlpatterns = [
    path('hello/', views.say_hello),
    path('test/', views.adding_template)
]